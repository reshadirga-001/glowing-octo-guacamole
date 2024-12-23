from flask import Flask, jsonify, request
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Supabase client
supabase = create_client(
    "https://pbwjxpjyhqodgchribby.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBid2p4cGp5aHFvZGdjaHJpYmJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM0NzQxMTEsImV4cCI6MjA0OTA1MDExMX0.wvSFKUlKyHX0HuWDjpUBJGFfmHkppJDdk8pZ07cBvQY"
)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    try:
        # You can customize the table name and query as needed
        response = supabase.table('researcher_list_2024').select("*").is_('scopus_id', 'null').limit(1).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update-data', methods=['POST'])
def update_data():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        # You can customize the table name and update conditions
        response = supabase.table('researcher_list_2024').update(data).eq('uuid', data.get('uuid')).execute()        
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
