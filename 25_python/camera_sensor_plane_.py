import time
import start
from numpy import real

#Create an operating system that automatically inputs plane data from sensors after takeoff and landing. 
#The system should log the data, analyze it for any anomalies, and generate a report for the flight crew.

print ('Enter plane number:')")
plane_number = input()

#Satellites in sky to use camera sensors to get plane data in real time 
start.camera_sensors(plane_number)

def camera_sensors(plane_number):
    print(f"Camera sensors activated for plane {plane_number}.")
    # Simulate data input every 5 seconds
    system = PlaneDataSystem()
    for _ in range():  
        data = get_plane_data(plane_number)
        system.input_data(data)
        time.sleep()  
    report = system.generate_report()
    print(report)
    return report



#Get plane data to assist with the simulation of the operating system prior to takeoff and landing 
def get_plane_data(plane_number):
    # Simulate getting data from sensors
    return {
        'plane_number': plane_number,
        'altitude': real(30000),  # in feet
        'speed': real(450),        # in knots
        'fuel_level': real(75),    # in percentage
        'engine_status': 'normal',  # could be 'normal', 'warning', 'critical'
        'physical_deterioration': 'none'  # could be 'none', 'minor', 'major'
        if sensors.detect_physical_deterioration():
            evaluate_physical_deterioration_level = 'minor' if sensors.detect_minor_deterioration() else 'major'
        else:
            evaluate_physical_deterioration_level = 'none'
    }

    #Supplier parts and maintenance data
    supplier_parts = {
        'engine': 'SupplierA',
        'wings': 'SupplierB',
        'landing_gear': 'SupplierC'
    }
    maintenance_data = {
        'engine': 'Last serviced on 2023-01-15',
        'wings': 'Last inspected on 2023-02-20',
        'landing_gear': 'Last checked on 2023-03-10'
    }

    if any(part for part in supplier_parts if part == 'faulty'):
        res turn {'error': 'Faulty parts detected from supplier.'}
    return data

def report_system():
   #A real-time data report about a specific supplier and history of faulty parts 

    def __init__(self):
        self.data_log = []

    def input_data(self, data):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.data_log.append((timestamp, data))
        print(f"Data logged at {timestamp}: {data}")

    def analyze_data(self):
        anomalies = []
        for timestamp, data in self.data_log:
            if data['altitude'] < 0 or data['speed'] < 0:
                anomalies.append((timestamp, data))
        return anomalies

    def generate_report(self):
        anomalies = self.analyze_data()
        report = "Flight Data Report\n"
        report += "=================\n"
        report += f"Total Data Points: {len(self.data_log)}\n"
        report += f"Anomalies Detected: {len(anomalies)}\n"
        for timestamp, data in anomalies:
            report += f"Anomaly at {timestamp}: {data}\n"
        return report
    
    def predictive_maintenance(self):
        maintenance_needed = []
        for timestamp, data in self.data_log:
            if data['engine_status'] == 'warning' or data['physical_deterioration'] in ['minor', 'major']:
                maintenance_needed.append((timestamp, data))
        return maintenance_needed
    
    def system_data_log(self):
        rows, columns = len(self.data_log), len(self.data_log[0]) if self.data_log else 0
        return rows, columns

class sensors:
    @staticmethod
    def detect_physical_deterioration():
        # Simulate detection logic
        return False  # Change as needed for testing

    @staticmethod
    def detect_minor_deterioration():
        # Simulate detection logic
        return False  # Change as needed for testing
    
    class start:
        @staticmethod
        def camera_sensors(plane_number):
            print(f"Camera sensors activated for plane {plane_number}.")
            # Simulate data input every 5 seconds
            system = PlaneDataSystem()
            for _ in range(5):  
                data = get_plane_data(plane_number)
                system.input_data(data)
                time.sleep(5)  
            report = system.generate_report()
            print(report)

    class live_camera:
        #camera angles and zooming in motion all around the plane on ground and in sky
        @staticmethod
        def camera_angles(plane_number):
            camera_angles = ['front', 'back', 'left', 'right', 'top', 'bottom']
            for angle in camera_angles:
                return f"Camera angle {angle} activated for plane {plane_number}."
            


            



    print("recommended_maintenance:", system.predictive_maintenance())
    print("columns and rows of data_log:", system.system_data_log())