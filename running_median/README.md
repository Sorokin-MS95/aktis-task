# Running Median task
#### General information
This is a demo app to calculate the running median of a list.
#### Installation instuctions

1. Create and activate virtual environment
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```
    **Note**: You can have another `python*` binary in your OS.

2. Change to running_median folder
    ```
    cd running_median
    ```
3. Run application using command
    ```
    python main.py
    ```
**Note:** You can pass input file using `--file`, `-f` argument. File path can be both absolute or relative name:

**Example:**
```
python main.py --file=input.txt
```