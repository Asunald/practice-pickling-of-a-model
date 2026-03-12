"""
上传模型到Huggingface Hub
"""
import os
import time
from huggingface_hub import HfApi, create_repo, login

def upload_model():
    """上传模型到Huggingface"""
    # 从环境变量获取token
    token = os.environ.get('HF_TOKEN')
    if not token:
        raise ValueError("❌ 未找到 HF_TOKEN 环境变量！请在GitHub Secrets中设置。")
    
    # 配置
    repo_id = "Small-Start/practice-pickling-of-a-model"  # 修改为你的用户名
    
    print(f"🚀 开始上传模型到 {repo_id}...")
    print(f"🔑 Token前缀: {token[:10]}...")
    
    # 先登录
    try:
        login(token=token)
        print("✅ Huggingface登录成功")
    except Exception as e:
        print(f"❌ 登录失败: {e}")
        raise
    
    # 创建API实例
    api = HfApi(token=token)
    
    # 创建仓库（如果不存在）
    try:
        url = create_repo(
            repo_id=repo_id,
            token=token,
            repo_type="model",
            exist_ok=True,
            private=False
        )
        print(f"✅ 仓库已创建/确认: {repo_id}")
        print(f"📍 仓库URL: {url}")
        
        # 等待仓库完全创建
        time.sleep(2)
        
    except Exception as e:
        print(f"⚠️  创建仓库时出现问题: {e}")
        print(f"⚠️  尝试继续上传...")
    
    # 上传模型文件夹
    try:
        print("📤 开始上传文件...")
        api.upload_folder(
            folder_path="model",
            repo_id=repo_id,
            repo_type="model",
            token=token,
            commit_message="🤖 自动训练并上传模型"
        )
        print(f"✅ 模型已成功上传到 https://huggingface.co/{repo_id}")
    except Exception as e:
        print(f"❌ 上传失败: {e}")
        print(f"💡 请检查:")
        print(f"   1. Token是否有写入权限")
        print(f"   2. 用户名是否正确: Small-Start")
        print(f"   3. 是否已在Huggingface登录")
        raise

if __name__ == "__main__":
    upload_model()
