import picoweb
import soil_moisture

# Shows webserver ip on microcontroller boot up on attached OLED display
display_ip()
    
app = picoweb.WebApp(__name__)
 
@app.route("/")
def index(req, resp):
    # Turn OLED display off
    display_off()
    
    # Reads soil sensors values and insetrs it into a list 
    soil_sensors = list()
    soil_sensors.append(soil_moisture.show_readings(33))
    soil_sensors.append(soil_moisture.show_readings(34))
    soil_sensors.append(soil_moisture.show_readings(35))
     
    yield from picoweb.start_response(resp, content_type = "text/html")
    yield from app.render_template(resp, "index.html", (soil_sensors,) )
    
ip = station.ifconfig()[0]
app.run(debug=True, host = ip, port = 80)
