from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the factory (you can replace with real data or a database later)
factory_info = {
    "name": "Uniform wala",
    "description": "We specialize in high-quality uniforms for schools, offices, and events. Custom orders available.",
    "location": "Purkhu , Akhnoor Road, Jammu",
    "contact": "info@uniformwala.com | +91 9419105832"
}

products = [
    {"name": "School Uniforms", "description": "Durable and comfortable for students.", "price": "$25"},
    {"name": "Office Blazers", "description": "Professional attire for corporate settings.", "price": "$50"},
    {"name": "Event Jackets", "description": "Customizable for parties and sports.", "price": "$40"}
]

@app.route('/')
def home():
    return render_template('index.html', title="Welcome to Uniform wala")

@app.route('/about')
def about():
    return render_template('about.html', info=factory_info, title="About Us")

@app.route('/products')
def products_page():
    return render_template('products.html', products=products, title="Our Products")

@app.route('/contact')
def contact():
    return render_template('contact.html', info=factory_info, title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)