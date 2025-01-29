from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Configure o logging para depuração
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Insira seu token do bot aqui
TOKEN = "8198035471:AAF28GeMaDbA66MnmNEDccpQZuMHnpXPDag"

# Defina um comando de boas-vindas
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Olá! Eu sou seu bot de cinema!")

# Função principal para iniciar o bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Adicionar comandos
    app.add_handler(CommandHandler("start", start))

    # Rodar o bot
    app.run_polling()

if __name__ == "__main__":
    main()
