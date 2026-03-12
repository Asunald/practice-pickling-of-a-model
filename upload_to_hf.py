"""
上传模型到Huggingface Hub
"""
import os
from huggingface_hub import HfApi, create_repo

def upload_model():
    """上传模型到Huggingface"""
    # 从环境变量获取token
    token = os.environ.get('HF_TOKEN')
    if not token:
        raise ValueError("❌ 未找到 HF_TOKEN 环境变量！请在GitHub Secrets中设置。")
    
    # 配置
    repo_id = "Asunald/practice-pickling-of-a-model"  # 修改为你的用户名
    
    print(f"🚀 开始上传模型到 {repo_id}...")
    
    # 创建API实例
    api = HfApi()
    
    # 创建仓库（如果不存在）
    try:
        create_repo(
            repo_id=repo_id,
            token=token,
            repo_type="model",
            exist_ok=True
        )
        print(f"✅ 仓库已创建/确认: {repo_id}")
    except Exception as e:
        print(f"⚠️  创建仓库时出现问题: {e}")
    
    # 上传模型文件夹
    try:
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
        raise

if __name__ == "__main__":
    upload_model()
