from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

def build_model(preprocessor):

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000))
        ]
    )

    return model