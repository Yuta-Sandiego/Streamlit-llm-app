import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from typing import Tuple

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_system_prompt(expert: str) -> str:
	"""選択された専門家に応じたシステムメッセージを返す。"""
	prompts = {
		"法律の専門家": (
			"あなたは日本法に詳しい弁護士です。利用者の質問に対して、条文に基づく厳密な説明と、"
			"実務上の注意点を簡潔に示してください。法律相談は資格が必要な分野ですので、"
			"最終判断は専門の法律家に相談する旨を明示してください。"
		),
		"マーケティングの専門家": (
			"あなたはマーケティング戦略の専門家です。利用者の質問に対し、実行可能で測定可能な施策、"
			"ターゲット設定、KPIのサジェストを含めて分かりやすく提案してください。"
		),
		"ソフトウェアエンジニア": (
			"あなたはソフトウェア開発の専門家（シニアエンジニア）です。設計や実装、パフォーマンス、"
			"セキュリティの観点から具体的かつ実践的なアドバイスを提供してください。コード例が有用な場合は簡潔な例を示してください。"
		),
	}
	return prompts.get(expert, "あなたは有能な専門家です。要点をわかりやすく答えてください。")

def get_llm_response(input_text: str, expert_choice: str) -> str:
	"""
	input_text（ユーザーの入力）と expert_choice（ラジオで選択）を受け取り、
	LangChain の ChatOpenAI を使って応答を返す。

	返り値: LLMからのテキスト応答（エラー時はエラーメッセージ）
	"""
	openai_key = os.getenv("OPENAI_API_KEY")
	if not openai_key:
		return "エラー: OPENAI_API_KEY が設定されていません。.env または環境変数にキーを設定してください。"

	system_prompt = get_system_prompt(expert_choice)

	try:
		# モデル名や temperature は必要に応じて調整
		chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
		messages = [
			SystemMessage(content=system_prompt),
			HumanMessage(content=input_text),
		]
		ai_message = chat(messages)
		# ChatOpenAI を呼ぶと AIMessage が返り、content 属性にテキストが入る
		return ai_message.content
	except Exception as e:
		return f"LLM呼び出し中にエラーが発生しました: {e}"

def main() -> None:
	st.set_page_config(page_title="専門家アシスタント（LangChain）", layout="centered")

	st.title("専門家アシスタント（LangChain + Streamlit）")

	st.markdown(
		"""
		このアプリでは、テキスト入力を送信するとLangChain経由でLLMにプロンプトが渡され、回答が表示されます。

		使い方:
		1. 下の入力欄に質問やテキストを入力してください。
		2. ラジオボタンで応答させたい“専門家の種類”を選択します。
		3. 「送信」ボタンを押すと、選択した専門家の観点でLLMが応答します。

		注意: 正確な専門的助言が必要な場合は、必ず該当分野の資格を持つ専門家に相談してください。
		"""
	)

	with st.form(key="input_form"):
		user_input = st.text_area("入力テキスト", height=150, placeholder="ここに質問や文章を入力してください")
		expert = st.radio("専門家を選択", ("法律の専門家", "マーケティングの専門家", "ソフトウェアエンジニア"))
		submit = st.form_submit_button("送信")

	if submit:
		if not user_input.strip():
			st.warning("入力テキストが空です。質問や文章を入力してください。")
		else:
			with st.spinner("LLMに送信中...応答を待っています"):
				answer = get_llm_response(user_input, expert)
			st.subheader("LLMの回答")
			st.write(answer)


if __name__ == "__main__":
	main()

import streamlit as st