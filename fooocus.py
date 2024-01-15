from comfy.samplers import *
import modules.core as core
import modules.patch as patch



class FooocusKSampler:  

    @classmethod
    def INPUT_TYPES(s):    
        return {
            "required":{ 
                "model": ("MODEL",),
                "positive": ("CONDITIONING", ),
                "negative": ("CONDITIONING", ),
                "latent_image": ("LATENT", ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2**63 - 1}),
                "steps": ("INT", {"default": 30, "min": 1, "max": 10000}),                   
                "cfg": ("FLOAT", {"default": 4.0, "min": 0.0, "max": 100.0}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"default": "dpmpp_2m_sde_gpu", }),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"default": "karras", }),                 
                "denoise": ("FLOAT", {"default": 1.0, "min": 0, "max": 1.0, "step": 0.1}),                 
                "adaptive_cfg":("FLOAT", {"default": 7, "min": 0.0, "max": 100.0}), 
                "sharpness": ("FLOAT", {"default": 2.0, "min": 0.0, "max": 100.0}),  
                "adm_scaler_positive":  ("FLOAT", {"default": 1.5, "min": 0.0, "max": 3.0,"step":0.1}),                
                "adm_scaler_negative":  ("FLOAT", {"default": 0.8, "min": 0.0, "max": 3.0,"step":0.1}),                
                "adm_scaler_end":  ("FLOAT", {"default": 0.3, "min": 0.0, "max": 1.0,"step":0.1}), 
            }
        }    

    RETURN_TYPES = ("LATENT",)
    FUNCTION = 'Fooocus_KSampler'
    CATEGORY = '17Reoucher'

    def Fooocus_KSampler(self,model,positive,negative,latent_image,seed, steps, cfg,sampler_name, scheduler,denoise,
                        sharpness,adaptive_cfg,adm_scaler_positive,adm_scaler_negative,adm_scaler_end):
        patch.patch_all()        
        patch.sharpness=sharpness
        patch.adaptive_cfg=adaptive_cfg
        patch.positive_adm_scale=adm_scaler_positive
        patch.negative_adm_scale=adm_scaler_negative
        patch.adm_scaler_end=adm_scaler_end      
        latent= core.ksampler(model=model,
                      positive=positive,
                      negative=negative,
                      latent=latent_image,
                      seed=seed,
                      steps=steps,
                      cfg=cfg,
                      sampler_name=sampler_name,
                      scheduler=scheduler,
                      denoise=denoise,                   
                      )
        patch.unpatch_all()
        return (latent,)
        
        