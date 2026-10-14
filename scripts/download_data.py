from ucimlrepo import fetch_ucirepo, list_available_datasets
from pathlib import Path
import os
"""
This script used to downlaod the dataset like bank marketing for this projects experimentation.

"""

def download_dataset(
    id_dataset: int,
    dataset_name: str = 'dataset'
):
    
    """
    Args:
        id_dataset: the id for dataset that you want download
        
    Returns:
        data: {
            variables: the list of variables in dataset
            features: the features of dataset
            target: the target of dataset
            metadata: the rest of dataset
        }
    
    """
    # the path to store the dataset
    root_dir = Path(__file__).resolve().parent.parent
    data_dir = root_dir / "data"
    data_dir.mkdir(parents=True ,exist_ok=True)
    # fetch the dataset
    dataset = fetch_ucirepo(id = id_dataset)
    
    # dataframe as pandas
    x = dataset.data.features
    y = dataset.data.target
    variables = dataset.variables
    
    
    # store to csv
    x_path = data_dir / f"{dataset_name}_features.csv"
    y_path = data_dir / f"{dataset_name}_target.csv"
    # var_path = data_dir / f"{dataset_name}_variables.csv"
    
    x.to_csv(x_path, index=False)
    y.to_list(y_path, index=False)
    # variables.to_csv(var_path, index=False)
    return x, y, variables

if __name__=="__main__":
    
    x, y, variables = download_dataset(id_dataset=222)
    
    print(x)
#id=222
    

    
