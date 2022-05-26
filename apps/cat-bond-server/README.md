# cat-bond-server  

### Install
```
conda env create -f anaconda_env.yml

conda activate cat-bond-server
```

### If you doubt it, dockerize it
```
docker build -t cat-bond-server:latest .

docker run -p 7000:7000 --net=host -t cat-bond-server:latest
```
