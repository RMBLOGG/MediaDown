# app.py - Main Flask Application for Vercel
from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import quote

app = Flask(__name__)

# ==================== ROUTES ====================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tiktok')
def tiktok():
    return render_template('tiktok.html')

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/spotify')
def spotify():
    return render_template('spotify.html')

@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

# ==================== API ENDPOINTS ====================

@app.route('/api/download/tiktok', methods=['POST'])
def api_tiktok():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/tiktok?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/facebook', methods=['POST'])
def api_facebook():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/facebook?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/instagram', methods=['POST'])
def api_instagram():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/instagram?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/twitter', methods=['POST'])
def api_twitter():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/twitter?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/spotify', methods=['POST'])
def api_spotify():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/spotify?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/ytmp3', methods=['POST'])
def api_ytmp3():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/ytmp3?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/download/ytmp4', methods=['POST'])
def api_ytmp4():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'success': False, 'message': 'URL tidak boleh kosong'}), 400

        encoded_url = quote(url, safe='')
        api_url = f'https://magma-api.biz.id/download/ytmp4?url={encoded_url}'
        
        response = requests.get(api_url, headers=get_headers(), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if not result.get('status', False):
                return jsonify({'success': False, 'message': result.get('message', 'API error')})
            return jsonify({'success': True, 'result': result.get('result', {})})
        else:
            return jsonify({'success': False, 'message': f'API Error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/about')
def about():
    return render_template('about.html')

# ==================== HELPER FUNCTIONS ====================

def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
    }

# ==================== VERCEL HANDLER ====================
# This is important for Vercel deployment
# Don't use app.run() for Vercel

# For local development only
if __name__ == '__main__':
    app.run(debug=True)