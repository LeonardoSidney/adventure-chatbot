# adventure-chatbot
An attempt to create an environment that can instruct a language model to behave as a world master.

# Warning 
It's more than obvious that this doesn't work, I made a commit to maintain version control and prevent me from doing anything unrecoverable.

# Install
Developed with python3.12 and Pytorch Rocm 6.2 (probably works on Nvidia) using Linux as a testing platform.

## Note
The use of `$` means that the command must be executed in your terminal with your normal user. And it shouldn't be copied.

## venv
You will need to create a virtual environment to download the dependencies.
```sh
$ python3.12 -m venv venv
```

## Pytorch
First you need to get pytorch for your graphics card.

### AMD
```sh
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
```

## requirements
For now the dependencies are the most current. So a pip install "should" suffice.
```sh
$ pip install -r requirements.txt
```

## script
I don't guarantee that the script works, but it seems to work.

```sh
$ chmod +x enviroments.sh
$ mv enviroments-user.sh.example enviroments-user.sh
$ chmod +x enviroments-user.sh
$ ./start.sh
```