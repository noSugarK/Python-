## python命令

### 检查Python版本

```bash
python -V
```

### 安装pip

```bash
python -m ensurepip
```



## pip命令

tips：
对于虚拟环境中的pip如果和conda环境中的pip版本不一致可能会导致报错，请更新pip版本一致

### 检查pip版本

```bash
pip -V
# pip --version
# pip show pip
```

### 更新pip版本

```bash
pip install --upgrade pip
```

### 查看已安装的软件包

```bash
pip list
```

### 安装软件包

```bash
pip install [库名]
```

### 查看安装的库的详细信息

```bash
pip show [库名]
```

### 更新软件包

```bash
pip install --upgrade [库名]
```

### 查看需更新的库

```bash
pip list --outdated
# pip list -o
```

### 卸载第三方库

```bash
pip uninstall [库名]
```

