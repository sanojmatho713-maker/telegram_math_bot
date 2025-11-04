from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import sympy as sp

async def start(update: Update, context):
    await update.message.reply_text("नमस्ते! मैं Math Solver Bot हूँ 🧮\nकोई भी सवाल भेजो — मैं हल कर दूँ!")

async def solve_math(update: Update, context):
    question = update.message.text
    try:
        expr = sp.sympify(question)
        ans = sp.simplify(expr)
        await update.message.reply_text(f"उत्तर: {ans}")
    except Exception:
        await update.message.reply_text("माफ करना, मैं इस सवाल को समझ नहीं पाया 😅\nउदाहरण: 2+3*5 या (x**2+2*x+1)")

app = ApplicationBuilder().token("8574270951:AAF0aEd56pYr14LRM1hknUNZ4PnOJGOGBds").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, solve_math))
app.run_polling()
