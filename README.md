# 这是一个2D地牢游戏

## 技术栈
- Python3.11+
- Pygame
- Esper (ECS架构)
- Uv (项目管理)

## 开始

### 1. 克隆仓库
```bash
git clone https://github.com/wanyi8181/delao
```

### 2. 安装依赖(没有uv的请先`pip install uv`)
```bash
uv sync 
```

### 3. 运行项目
```bash
uv run main.py
```

## 开发者注意事项
- 请使用`uv`进行项目管理(`uv add 包名`)，不要直接使用`pip`安装依赖
- 严禁直接操作`main`分支,不要本地操作`dev`分支

### 贡献方法
在`dev`分支上新建`feat/你的新功能名`分支, 开发完成之后提交pr等待开发者审核合并到`dev`分支