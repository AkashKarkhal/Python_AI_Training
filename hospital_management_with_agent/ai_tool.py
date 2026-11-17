from langchain_core.tools import tool

patients = {}
appointments = {}

doctors = {
    "D201": {
        "name": "Dr Amit",
        "specialization": "Cardiology",
        "slots": ["10:00", "11:00"]
    },
    "D202": {
        "name": "Dr Priya",
        "specialization": "Neurology",
        "slots": ["09:00", "10:00"]
    }
}

medical_records = {
    "P1001": {
        "history": ["Diabetes"],
        "allergies": ["Dust"]
    }
}

@tool
def register_patient(
    full_name:str,
    age:int,
    phone:str,
    symptoms:str=""
):
    """Register a patient"""

    patient_id = f"P{1000 + len(patients)+1}"

    patients[patient_id] = {
        "name": full_name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms
    }

    return {
        "patient_id": patient_id,
        "status": "success"
    }
    
@tool
def check_doctor_availability(
    specialization:str
):
    """Check doctor availability"""

    return [
        {
            "doctor_id": doctor_id,
            "doctor_name": doctor["name"],
            "slots": doctor["slots"]
        }
        for doctor_id, doctor in doctors.items()
        if doctor["specialization"].lower() == specialization.lower()
    ]
    
    
@tool
def book_appointment(
    patient_id:str,
    doctor_id:str,
    time_slot:str
):
    """Book appointment"""

    appointment_id = f"A{5000 + len(appointments)+1}"

    appointments[appointment_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "time_slot": time_slot
    }

    return {
        "appointment_id": appointment_id,
        "status": "success"
    }
    
@tool
def get_patient_medical_records(
    patient_id:str,
    authorized_role:str
):
    """Get patient records"""

    if authorized_role not in ["doctor", "admin"]:
        return {"message":"Access denied"}

    return medical_records.get(
        patient_id,
        {"message":"Patient not found"}
    )
    
    
@tool
def calculate_hospital_bill(
    consultation_fee:float,
    lab_charges:float,
    treatment_charges:float,
    discount_percent:float=0
):
    """Calculate hospital bill"""

    subtotal = (
        consultation_fee +
        lab_charges +
        treatment_charges
    )

    discount = subtotal * discount_percent / 100

    return {
        "subtotal": subtotal,
        "discount": discount,
        "total": subtotal - discount
    }            
    