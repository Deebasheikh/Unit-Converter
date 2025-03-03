import streamlit as st

# Set Page Config
st.set_page_config(page_title="Unit Converter")

# FontAwesome Icons (For Better UI)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
        border-radius: 10px !important;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #008080 !important;
        color: white !important;
        border: none;
    }
    .stButton>button:hover {
        background-color: #006666 !important;
    }
    .stSuccess {
        font-size: 20px;
        font-weight: bold;
        color: #008000;
    }
    .formula-box {
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title with Icon
st.markdown('<h1><i class="fas fa-exchange-alt"></i> Unit Converter</h1>', unsafe_allow_html=True)
st.write("Convert between different units easily!")

# Categories Dropdown
category = st.selectbox("Select Category", [
    "Length", "Mass", "Area", "Volume", "Temperature", 
    "Time", "Speed", "Pressure", "Energy", 
    "Frequency", "Fuel Economy", "Data Transfer Rate", 
    "Digital Storage", "Plane Angle"
])

# Units List
units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
    "Mass": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Area": ["Square Meters", "Square Kilometers", "Square Miles", "Acres", "Hectares"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters", "Cubic Inches", "Gallons"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"],
    "Pressure": ["Pascals", "Bar", "PSI", "Atmospheres"],
    "Energy": ["Joules", "Calories", "Kilojoules", "Watt-hours"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Fuel Economy": ["Kilometers per liter", "Miles per gallon"],
    "Data Transfer Rate": ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second"],
    "Digital Storage": ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"],
    "Plane Angle": ["Degrees", "Radians"]
}

# Layout: 2 Columns
col1, col2 = st.columns(2)

# Input Value
with col1:
    input_value = st.number_input("Enter Value", min_value=0.0, step=0.1)

# Output Value Placeholder
with col2:
    st.write("")  # Adds spacing

# Layout: 2 Columns for Units
col3, col4 = st.columns(2)

# Input & Output Units
with col3:
    input_unit = st.selectbox("From", units[category])

with col4:
    output_unit = st.selectbox("To", units[category])

# Conversion Logic
def convert(value, input_unit, output_unit, category):
    if input_unit == output_unit:
        return value, "No conversion needed for same units."

    result = value
    formula = ""

    # Temperature Conversion
    if category == "Temperature":
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = (value * 9/5) + 32
            formula = f"({value}°C × 9/5) + 32 = {result}°F"
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = value + 273.15
            formula = f"{value}°C + 273.15 = {result}K"
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = (value - 32) * 5/9
            formula = f"({value}°F - 32) × 5/9 = {result}°C"
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
            formula = f"(({value}°F - 32) × 5/9) + 273.15 = {result}K"
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = value - 273.15
            formula = f"{value}K - 273.15 = {result}°C"
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
            formula = f"(({value}K - 273.15) × 9/5) + 32 = {result}°F"
        return result, formula

    # General Conversions
    conversion_factors = {
        "Length": {
            "Meters": 1, 
            "Kilometers": 1000, 
            "Centimeters": 0.01, 
            "Millimeters": 0.001,
            "Miles": 1609.34, 
            "Yards": 0.9144, 
            "Feet": 0.3048, 
            "Inches": 0.0254
        },
        "Mass": {
            "Grams": 1, 
            "Kilograms": 1000,
            "Pounds": 453.592, 
            "Ounces": 28.3495
        },
        "Area": {
            "Square Meters": 1, 
            "Square Kilometers": 1_000_000, 
            "Square Miles": 2_589_988,
            "Acres": 4046.86,
            "Hectares": 10_000
        },
        "Volume": {
            "Liters": 1, 
            "Milliliters": 0.001, 
            "Cubic Meters": 1000, 
            "Cubic Inches": 0.0163871, 
            "Gallons": 3.78541
        },
        "Time": {
            "Seconds": 1, 
            "Minutes": 60, 
            "Hours": 3600, 
            "Days": 86400, 
            "Weeks": 604800,
            "Months": 2.628e+6, 
            "Years": 3.154e+7
        },
        "Speed": {
            "Meters per second": 1, 
            "Kilometers per hour": 0.277778,
            "Miles per hour": 0.44704,
            "Knots": 0.514444
        },
        "Pressure": {
            "Pascals": 1, 
            "Bar": 100000, 
            "PSI": 6894.76, 
            "Atmospheres": 101325
        },
        "Energy": {
            "Joules": 1, 
            "Calories": 4.184, 
            "Kilojoules": 1000, 
            "Watt-hours": 3600
        },
        "Frequency": {
            "Hertz": 1,
              "Kilohertz": 1000, 
              "Megahertz": 1_000_000, 
              "Gigahertz": 1_000_000_000
        },
        "Fuel Economy": {
            "Kilometers per liter": 1,
            "Miles per gallon": 2.35215
        },
        "Data Transfer Rate": {
            "Bits per second": 1, 
            "Kilobits per second": 1000, 
            "Megabits per second": 1_000_000,
            "Gigabits per second": 1_000_000_000
        },
        "Digital Storage": {
            "Bits": 1, 
            "Bytes": 8, 
            "Kilobytes": 8_000, 
            "Megabytes": 8_000_000,
            "Gigabytes": 8_000_000_000, 
            "Terabytes": 8_000_000_000_000
        },
        "Plane Angle": {
            "Degrees": 1, 
            "Radians": 57.2958
        }
    }

      # General Conversion Logic
    if category in conversion_factors:
        factor_in = conversion_factors[category][input_unit]
        factor_out = conversion_factors[category][output_unit]
        result = value * factor_in / factor_out

        if factor_in > factor_out:
            formula = f"Multiply by {factor_in / factor_out}"
        else:
            formula = f"Divide by {factor_out / factor_in}"

    return result, formula

# Convert Button
if st.button("Convert Now"):
    result, formula = convert(input_value, input_unit, output_unit, category)
    st.success(f"Result: {result} {output_unit}")
    st.markdown(f'<div class="formula-box"><i class="fas fa-calculator"></i> <b>Formula:</b> {formula}</div>', unsafe_allow_html=True)
