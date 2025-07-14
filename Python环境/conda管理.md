## 管理conda


### 检查conda版本

```bash
conda --version
```

### 列出所有环境

用来查看conda创建的所有虚拟环境

```bash
conda env list
```

命令用于查看conda下的包

```bash
conda list
```

### 查看环境管理的全部命令帮助

```bash
conda env -h
```

### conda升级

我们可以在命令行中或者anaconda prompt中执行命令进行操作。

```bash
conda update conda	#升级conda
conda update anaconda	#升级anaconda前要先升级conda
conda update --all	#升级所有包
```

### conda升级后释放空间

在升级完成之后，我们可以使用命令来清理一些无用的包以释放一些空间：

```bash
conda clean -p	#删除没有用的包
conda clean -t	#删除保存下来的压缩文件（.tar）
```

## 管理环境

### 修改 `.condarc` 设置默认环境路径

如果你希望以后新建的所有环境都默认保存到某个位置（如 D 盘），可以编辑你的 `.condarc` 文件：

步骤如下：

1. 找到配置文件路径（你已经知道是 `C:\Users\86139\.condarc`）
2. 用记事本或 VS Code 打开它
3. 添加或修改以下内容：

```yaml
envs_dirs:
  - D:\conda_envs
  - C:\Users\86139\.conda\envs
```

这样以后运行 `conda create -n myenv ...` 时，Conda 将优先把环境创建在 `D:\conda_envs` 中。

### 创建虚拟环境

```bash
conda create -n env-name [list of package]
```

-n env-name是设置新建环境的名字，list of package是可选项，选择要为该环境安装的包。

如果我们没有指定安装python的版本，conda会安装我们最初安装conda时所装的那个版本的python。

若创建特定python版本的包环境，需键入conda create -n env-name python=3.6


```bash
conda create -n Django python==3.12.9 django
```

### 激活环境

Linux，OS X:

```bash
source activate env-name
```

Windows：

```bash
activate env-name
```

**小技巧：**

新的开发环境会被默认安装在你conda目录下的envs文件目录下。你可以指定一个其他的路径；

### 切换到base环境

如果要从你当前工作环境的路径切换到系统根目录时，键入：

Linux，OS X:

```bash
conda source deactivate
```

Windows:

```bash
conda deactivate
```

### 复制一个环境

通过克隆来复制一个环境。这儿将通过克隆snowfllakes来创建一个称为flowers的副本。

```bash
conda create -n flowers --clone snowflakes
```

通过`conda env list`来检查目前拥有的环境

### 删除一个环境

如果你不想要这个名为flowers的环境，就按照如下方法移除该环境：

```bash
conda env remove -n flowers
```

## 管理包

### 安装包 或 安装特定版本的包

```bash
conda install package-name
```

```bash
conda install package-name==version
```

### 查看所有已安装包

```bash
conda list
```

### 卸载包

```bash
conda remove package-name
```

### 更新包

更新一个包

```bash
conda update package-name
```

更新所有包

```bash
conda update --all
```

### 搜索包

可以模糊搜索

```bash
conda search search-term
```

