# Mouse prediction task
#### General information
This is a demo app to distinguish the meaning of words within sentences.
#### Installation instuctions

1. Create and activate virtual environment
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    **Note**: You can have another `python*` binary in your OS.

2. Change to mouse_prediction folder
    ```
    cd mouse_prediction
    ```
3. Run application using command
    ```
    python main.py
    ```
**Note:** You can pass input file using `--file`, `-f` argument. File path can be both absolute or relative name:
**Example**:
```
python main.py --file=input.txt
```