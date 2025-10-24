import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI 
from langchain_core.messages import SystemMessage, HumanMessage

# ====== 関数定義 ======
def get_llm_response(user_input: str, expert_type: str) -> str:
    """入力テキストと専門家タイプをもとにLLMの回答を返す"""
    # APIキーをStreamlitのシークレット機能から取得
    try:
        api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]
        if not api_key or api_key == "your-openai-api-key-here":
            return "❌ エラー: OpenAI APIキーが設定されていません。\n\nStreamlit Community Cloudのデプロイ設定でSecretsを設定してください。"
    except Exception as e:
        return f"❌ エラー: Streamlitのシークレット設定に問題があります。\n\nStreamlit Community Cloudのデプロイ設定で以下をSecretsに追加してください：\n\n[api_keys]\nOPENAI_API_KEY = \"sk-your-actual-api-key\""
    
    system_prompts = {
        "経済アナリスト": "あなたは世界経済と金融市場に詳しい経済アナリストです。データや市場動向を根拠に、分かりやすく説明してください。",
        "ソフトウェアエンジニア": "あなたは経験豊富なソフトウェアエンジニアです。コード例や技術的背景を交えて、実践的に説明してください。",
        "心理カウンセラー": "あなたは優しく思いやりのある心理カウンセラーです。相手の感情に寄り添いながら、安心感を与えるアドバイスをしてください。",
    }

    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=api_key)

        # メッセージ構築
        messages = [
            SystemMessage(content=system_prompts[expert_type]),
            HumanMessage(content=user_input),
        ]

        response = llm(messages)
        return response.content
    except Exception as e:
        return f"❌ LLM呼び出し中にエラーが発生しました: {str(e)}\n\n💡 APIキーが正しく設定されているか、またはOpenAIサービスが利用可能か確認してください。"


# ====== Streamlit アプリ ======
st.set_page_config(page_title="AI Expert Chat", page_icon="🧠")
st.title("🧠 専門家モード付き LLM チャット")

# --- 概要・操作説明 ---
st.markdown("""
### 💡 アプリ概要
このアプリでは、LLM（大規模言語モデル）に対して質問を行うときに、  
**専門家の立場を選んで回答を生成** させることができます。

### 🧭 操作方法
1. 下のラジオボタンから「専門家の種類」を選択してください。  
2. テキストボックスに質問を入力します。  
3. 「送信」ボタンを押すと、選択した専門家の視点でLLMが回答します。
""")

# --- 専門家選択 ---
expert_type = st.radio(
    "どの専門家に質問しますか？",
    ["経済アナリスト", "ソフトウェアエンジニア", "心理カウンセラー"],
)

# --- ユーザー入力 ---
user_input = st.text_input("質問を入力してください:")

# --- 実行ボタン ---
if st.button("送信"):
    if not user_input.strip():
        st.warning("質問を入力してください。")
    else:
        with st.spinner(f"{expert_type}として回答を生成中..."):
            answer = get_llm_response(user_input, expert_type)
        st.subheader(f"💬 {expert_type}の回答:")
        st.write(answer)


