import web
import requests
import json

urls = ('/movies?', 'Movies',)    
app = web.application(urls, globals())

class Movies:
    def GET(self): 
        parametros = web.input() # Parametros por URL           
        return self.datos(parametros) 	
    
    def datos(self,parametros):       
        text = parametros.texto
        datos={}
        key = "c1e68040-a234-11eb-a596-737817c68e7175821cc7-06da-45d4-9628-36672e20c69b"
        url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

        response = requests.get(url, params={ "data" : text })
        
        #print(response.text)
        
        #resul=response.text
        resultado = response.json()
        encoded = json.dumps(resultado)
        decoded = json.loads(encoded)
        class_name= resultado[0]["class_name"]
        confidence= resultado[0]["confidence"]
        classifierTimestamp= resultado[0]["classifierTimestamp"]
        datos["Clasificacion"]=class_name
        datos["confidence"]=confidence
        datos["classifierTimestamp"]=classifierTimestamp
        #print(datos)

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            return  json.dumps(datos)
        else:
            response.raise_for_status()
        return  json.dumps(datos)

if __name__ == "__main__":

    app.run()



