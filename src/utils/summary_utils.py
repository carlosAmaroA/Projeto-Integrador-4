import textwrap
from IPython.display import display, Markdown, clear_output
import pandas as pd
from pandas.api.types import is_integer_dtype,is_string_dtype,is_float_dtype
import ipywidgets as widgets 





def col_summary(dataset,name = ''):
    display(Markdown(f'#### **Dataset**: {name}'))
    integers = []
    floats = []
    factors = []
    generals = []
    for col_name in dataset.columns:
        column = dataset.loc[:,col_name]
        if len(column.unique())<10:
            factors.append(col_name) 
        elif is_integer_dtype(column):
            integers.append(col_name)
        elif is_float_dtype(column):
            floats.append(col_name)
        else:
            generals.append(col_name)
    default_layout = widgets.Layout(width='250px')
    empty_layout = widgets.Layout(width='100px')
    types = [integers,floats,factors,generals]
    labels = ['Integer','Float','Categorical','Generic Object']
    dropdowns = []
    outputs = []
    vboxs = []
    for i,type in enumerate(types):
        label = widgets.Label('Type: '+labels[i])
        dropdown = widgets.Dropdown(
            options=type or ['Empty'],
            value=type[0] if type else 'Empty',
            disabled=not bool(type),
            layout=default_layout if type else empty_layout
        )
        output = widgets.Output()
        dropdowns.append(dropdown)
        outputs.append(output)
        vboxs.append(widgets.VBox([label,dropdown,output]))
    
    def update(change=None):
        with outputs[0]:
            outputs[0].clear_output()
            if dropdowns[0].value != 'Empty':
                column = dataset.loc[:,dropdowns[0].value]
                cv = column.std()/column.mean() if column.mean() !=0 else 'Mean = 0'
                cv = f'{cv:.2f}' if isinstance(cv,int) else cv
                display(Markdown(f"**Mean:** {column.mean():.2f}"))
                display(Markdown(f"**Median:** {column.median():.2f}"))
                display(Markdown(f"**Std:** {column.std():.2f}"))
                display(Markdown(f"**CV:** {cv}"))
                display(Markdown(f"**Min:** {column.min():.2f}"))
                display(Markdown(f"**Max:** {column.max():.2f}"))
                display(Markdown(f"**Not Missing:** {column.count()}"))
                display(Markdown(f"**Missing:** {column.isna().sum()}"))
                display(Markdown(f"**Total:** {len(column)}"))
        with outputs[1]:
            outputs[1].clear_output()
            if dropdowns[1].value != 'Empty':
                column = dataset.loc[:,dropdowns[1].value]
                cv = column.std()/column.mean() if column.mean() !=0 else 'Mean = 0'
                display(Markdown(f"**Mean:** {column.mean():.2f}"))
                display(Markdown(f"**Median:** {column.median():.2f}"))
                display(Markdown(f"**Std:** {column.std():.2f}"))
                display(Markdown(f"**CV:** {cv:.2f}"))
                display(Markdown(f"**Min:** {column.min():.2f}"))
                display(Markdown(f"**Max:** {column.max():.2f}"))
                display(Markdown(f"**Not Missing:** {column.count()}"))
                display(Markdown(f"**Missing:** {column.isna().sum()}"))
                display(Markdown(f"**Total:** {len(column)}"))
        with outputs[2]:
            outputs[2].clear_output()
            if dropdowns[2].value != 'Empty':
                column = dataset.loc[:,dropdowns[2].value]
                factors = column.unique()
                cat = " | ".join(map(str, factors))
                cat = textwrap.wrap(cat,width=50,break_long_words=False)
                display(Markdown("**Categories:**"))
                display(Markdown('<br>'.join(cat)))  # ensure factors are strings
                display(Markdown('**Count:**'))
                for factor,count in column.value_counts().items():
                    display(Markdown(f'{factor}: {count}'))
                display(Markdown(f"**Not Missing:** {column.count()}"))
                display(Markdown(f"**Missing:** {column.isna().sum()}"))
                display(Markdown(f"**Total:** {len(column)}"))
        with outputs[3]:
            outputs[3].clear_output()
            if dropdowns[3].value != 'Empty':
                column = dataset.loc[:,dropdowns[3].value]
                display(Markdown(f"**Not Missing:** {column.count()}"))
                display(Markdown(f"**Missing:** {column.isna().sum()}"))
                display(Markdown(f"**Total:** {len(column)}"))
    
    for dropdown in dropdowns:
        dropdown.observe(update)
    
    update()
    display(widgets.HBox(vboxs))
