#This fuction has two forms of to categorize. First, all df. Second, with a one array of columns.
def as_factor(data, type_col="object", columns=[]):
    if len(columns)==0:
        v=data.select_dtypes(include=[type_col]).columns.tolist()
        for col in v:
            u=data[col].unique()
            data[col]=data[col].map({x:u.tolist().index(x) for x in u})
    else:
        for col in columns:
            u=data[col].unique()
            data[col]=data[col].map({x:u.tolist().index(x) for x in u})
    return data