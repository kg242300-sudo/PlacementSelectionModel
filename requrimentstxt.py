import pandas as pd
import sklearn

# Get the exact installed versions of packages used
pandas_ver = pd.__version__
sklearn_ver = sklearn.__version__

requirements_content = f"""pandas=={pandas_ver}
scikit-learn=={sklearn_ver}
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements_content)

print("Generated 'requirements.txt' with currently installed package versions:")
print(requirements_content)
#output 
#Generated 'requirements.txt' with currently installed package versions:
pandas==2.2.3
scikit-learn==1.6.1

