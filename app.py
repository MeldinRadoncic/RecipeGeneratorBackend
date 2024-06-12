
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
import replicate
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://recipe-generator-react-mu.vercel.app/","http://localhost:3000"]}})


# Load API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Initialize OpenAI API
llm = OpenAI(model="gpt-3.5-turbo-instruct")

@app.route('/api/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    food = data.get('food')
    calories = data.get('calories')
    language = data.get('language')

    # Generate Recipe
    prompt = PromptTemplate(
        input_variables=["food", "calories", "language"],
        template="""
            You are an experienced chef. Craft a recipe for {food} containing {calories} calories. Avoid employing symbols like -, +, *, or similar in the recipe. Instead of periods, utilize "Step" followed by the appropriate number for ordered lists, such as Step 1, Step 2, and so on and listen in columns.
            Answer on {language} language.
        """
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    recipe = llm_chain.run({
        "food": food,
        "calories": calories,
        "language": language
    })

    # Generate Image
    output = replicate.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input={"prompt": food},
    )

    image_url = output[0]

    return jsonify({
        "food": food,
        "calories": calories,
        "language": language,
        "recipe": recipe,
        "image_url": image_url
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
