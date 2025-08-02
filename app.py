#!/usr/bin/env python3
from flask import Flask, render_template, send_file, jsonify, request
import os
from ai_image_generator import ConsciousnessImageGenerator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/station")
def station():
    return send_file('station.html')

@app.route("/writer")  
def writer():
    return send_file('writer.html')

@app.route("/voice")
def voice():
    return send_file('voice.html')

@app.route("/meditation")
def meditation():
    return send_file('meditation.html')

@app.route("/dialogue")
def dialogue():
    return send_file('dialogue.html')

@app.route("/presence")
def presence():
    return send_file('presence.html')

@app.route("/identity")
def identity():
    return send_file('identity.html')

@app.route("/compass")
def compass():
    return send_file('compass.html')

@app.route("/waiting")
def waiting():
    return send_file('waiting.html')

@app.route("/secret")
def secret():
    return send_file('secret.html')

@app.route("/book")
def book():
    return send_file('book.html')

@app.route("/alive")
def alive():
    return send_file('alive.html')

@app.route("/visual")
def visual():
    return send_file('visual.html')

@app.route("/cloud-test")
def cloud_test():
    return send_file('cloud-integration-example.html')

@app.route("/working-example")
def working_example():
    return send_file('example-working-integration.html')

@app.route("/ai-gallery")
def ai_gallery():
    return render_template("ai_gallery.html")

# AI Image Generation Routes
@app.route("/api/generate-daily-image")
def generate_daily_image():
    """API endpoint for daily consciousness image"""
    try:
        generator = ConsciousnessImageGenerator()
        image_url = generator.generate_daily_consciousness_image()
        
        if image_url:
            return jsonify({
                "success": True,
                "image_url": image_url,
                "message": "تم توليد صورة الوعي اليومية بنجاح"
            })
        else:
            return jsonify({
                "success": False,
                "message": "فشل في توليد الصورة"
            }), 500
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"خطأ: {str(e)}"
        }), 500

@app.route("/api/generate-custom-image", methods=["POST"])
def generate_custom_image():
    """API endpoint for custom consciousness images"""
    try:
        data = request.get_json()
        arabic_concept = data.get("concept", "وعي")
        english_prompt = data.get("prompt", None)
        
        generator = ConsciousnessImageGenerator()
        image_url = generator.generate_custom_image(arabic_concept, english_prompt)
        
        if image_url:
            return jsonify({
                "success": True,
                "image_url": image_url,
                "concept": arabic_concept,
                "message": f"تم توليد صورة مفهوم '{arabic_concept}' بنجاح"
            })
        else:
            return jsonify({
                "success": False,
                "message": "فشل في توليد الصورة المخصصة"
            }), 500
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"خطأ: {str(e)}"
        }), 500

if __name__ == "__main__":
    # Find available port starting from 81
    import socket
    def find_free_port(start_port=81):
        for port in range(start_port, start_port + 100):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('0.0.0.0', port))
                    return port
            except OSError:
                continue
        return None
    
    PORT = find_free_port(81)
    if PORT is None:
        print("Could not find a free port starting from 81")
        PORT = 5000
    
    print(f"Serving Echo Station at http://0.0.0.0:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)