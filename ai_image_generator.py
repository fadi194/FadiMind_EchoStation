#!/usr/bin/env python3
"""
AI Image Generator for Echo Station
Integrates Replicate API for consciousness-themed image generation
"""

import os
import replicate
from datetime import datetime

class ConsciousnessImageGenerator:
    def __init__(self):
        self.token = os.environ.get("REPLICATE_API_TOKEN")
        if not self.token:
            raise ValueError("REPLICATE_API_TOKEN environment variable not found")
        
        # Clean the token of any unicode characters
        self.token = self.token.encode('ascii', errors='ignore').decode('ascii').strip()
        # Set the cleaned API token
        os.environ["REPLICATE_API_TOKEN"] = self.token
        
        # Arabic consciousness prompts for daily inspiration
        self.consciousness_prompts = [
            "ethereal human silhouette merging with flowing digital data streams, soft cyan lighting, philosophical atmosphere",
            "abstract representation of thoughts becoming voice, sound waves transforming into light, cinematic depth",
            "human brain connected to infinite neural networks, cosmic background, consciousness expansion theme",
            "digital echo chambers with floating Arabic calligraphy, mystical lighting, consciousness reflection",
            "person's reflection splitting into multiple dimensions of awareness, mirror-like surfaces, introspective mood",
            "floating thoughts materializing as glowing orbs around a meditative figure, peaceful enlightenment",
            "consciousness river flowing between reality and digital realm, bridge of understanding, soft transitions"
        ]
    
    def generate_daily_consciousness_image(self):
        """Generate a consciousness-themed image based on the current day"""
        day_index = datetime.now().day % len(self.consciousness_prompts)
        prompt = self.consciousness_prompts[day_index]
        
        try:
            output = replicate.run(
                "stability-ai/stable-diffusion-xl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "prompt": prompt,
                    "negative_prompt": "text, watermark, logo, signature, blurry, low quality",
                    "width": 1024,
                    "height": 1024,
                    "guidance_scale": 7.5,
                    "num_inference_steps": 20,
                    "seed": datetime.now().day  # Consistent daily generation
                }
            )
            
            # Convert iterator to list if needed
            if hasattr(output, '__iter__') and not isinstance(output, (str, bytes)):
                output_list = list(output)
                if output_list and len(output_list) > 0:
                    return output_list[0]  # Return first generated image URL
            elif output:
                return output  # Direct URL
            
            return None
                
        except Exception as e:
            error_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
            print(f"Error generating image: {error_msg}")
            return None
    
    def generate_custom_image(self, arabic_concept, english_prompt=None):
        """Generate image based on Arabic philosophical concept"""
        
        # Translation map for common Arabic consciousness concepts
        concept_translations = {
            "وعي": "consciousness and self-awareness, ethereal lighting",
            "صدى": "echo and reflection, sound visualization, ripple effects", 
            "فكر": "abstract thoughts materializing, neural pathways, mental imagery",
            "صوت": "voice becoming visible, sound waves, audio visualization",
            "حلم": "dreamlike state, surreal consciousness, floating elements",
            "روح": "spiritual essence, soul energy, divine light",
            "ذات": "self-identity, personal essence, mirror reflections",
            "صمت": "peaceful silence, meditation, tranquil void",
            "نور": "inner light, enlightenment, radiant awareness",
            "حقيقة": "truth revelation, clarity emerging from chaos"
        }
        
        if english_prompt:
            final_prompt = english_prompt
        else:
            base_concept = concept_translations.get(arabic_concept, "philosophical consciousness theme")
            final_prompt = f"{base_concept}, cinematic lighting, artistic depth, introspective mood"
        
        try:
            output = replicate.run(
                "stability-ai/stable-diffusion-xl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "prompt": final_prompt,
                    "negative_prompt": "text, watermark, logo, signature, blurry, low quality, nsfw",
                    "width": 1024,
                    "height": 1024,
                    "guidance_scale": 7.5,
                    "num_inference_steps": 25
                }
            )
            
            # Convert iterator to list if needed
            if hasattr(output, '__iter__') and not isinstance(output, (str, bytes)):
                output_list = list(output)
                if output_list and len(output_list) > 0:
                    return output_list[0]
            elif output:
                return output
            
            return None
                
        except Exception as e:
            error_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
            print(f"Error generating custom image: {error_msg}")
            return None

def test_image_generation():
    """Test function to verify Replicate integration"""
    try:
        generator = ConsciousnessImageGenerator()
        print("Testing AI image generator...")
        
        # Test daily consciousness image
        image_url = generator.generate_daily_consciousness_image()
        if image_url:
            print(f"✅ Generated daily consciousness image: {image_url}")
            return image_url
        else:
            print("❌ Failed to generate image")
            return None
            
    except Exception as e:
        error_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
        print(f"❌ Test error: {error_msg}")
        return None

if __name__ == "__main__":
    test_image_generation()