from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

def groq_response(content):

    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hey! I am a bot created by Sidaarth Gupta (do64caqi). How can I help you?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    try:
        bot_response = groq_response(user_message)
        await update.message.reply_text(bot_response)
    except Exception as e:
        await update.message.reply_text("Sorry, I couldn't process your request.")
        print(f"Error: {e}")

def main():
    application = Application.builder().token("7599067026:AAFV3LWZV7PdtZ18I6eGqEYartZSWcNlSIo").build() #Telegram API Token
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()