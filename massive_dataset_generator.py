import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

# Initialize Faker for realistic text generation
fake = Faker()

# --- MASTER CONFIGURATION DICTIONARY ---
# This holds ALL 50 dataset schemas and rules on how to generate data for them.
DATASETS = {
    "1": {
        "name": "Health & Medicine - Electronic Health Records",
        "columns": [
            ("patient_id", "id"), ("admission_date", "date_2024"), ("systolic_bp", "bp_sys"), 
            ("diastolic_bp", "bp_dia"), ("lab_result_value", "float_50_200"), 
            ("diagnosis_code", "icd10")
        ]
    },
    "2": {
        "name": "Medical Imaging (Metadata)",
        "columns": [
            ("image_id", "id"), ("modality", "choice_['MRI','CT','X-Ray','Ultrasound']"), 
            ("body_part", "choice_['Brain','Chest','Spine','Abdomen','Knee']"), 
            ("bounding_box_coordinates", "bbox"), ("pixel_spacing", "float_0.1_1.5"), 
            ("pathology_label", "choice_['Benign','Malignant','Normal']")
        ]
    },
    "3": {
        "name": "Genomics",
        "columns": [
            ("sample_id", "id"), ("chromosome", "choice_['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y']"), 
            ("position", "int_1_250000000"), ("reference_allele", "choice_['A','T','C','G']"), 
            ("altered_allele", "choice_['A','T','C','G']"), 
            ("mutation_type", "choice_['Missense','Deletion','Insertion','Frameshift','Nonsense']")
        ]
    },
    "4": {
        "name": "Pharmacovigilance",
        "columns": [
            ("report_id", "id"), ("drug_name", "drug"), ("dosage_mg", "int_5_1000"), 
            ("adverse_event", "adverse"), ("severity_score", "int_1_5"), 
            ("outcome", "choice_['Recovered','Hospitalized','Fatal']")
        ]
    },
    "5": {
        "name": "Public Health",
        "columns": [
            ("region_code", "region"), ("report_week", "date_week"), 
            ("cases_reported", "int_0_5000"), ("vaccination_rate", "pct"), 
            ("hospital_bed_occupancy", "pct"), ("mortality_count", "int_0_500")
        ]
    },
    "6": {
        "name": "Wearable Health",
        "columns": [
            ("user_id", "id"), ("timestamp", "datetime"), ("heart_rate_bpm", "int_40_180"), 
            ("step_count", "int_0_15000"), ("sleep_stage", "choice_['Deep','Light','REM','Awake']"), 
            ("calories_burned", "int_50_1000")
        ]
    },
    "7": {
        "name": "Stock Market",
        "columns": [
            ("ticker_symbol", "ticker"), ("trade_date", "date_2024"), 
            ("open_price", "float_10_500"), ("high_price", "float_10_500"), 
            ("close_price", "float_10_500"), ("volume", "int_1000_10000000")
        ]
    },
    "8": {
        "name": "Credit Scoring",
        "columns": [
            ("applicant_id", "id"), ("annual_income", "int_20000_250000"), 
            ("debt_to_income_ratio", "float_0_1"), ("missed_payments_2yr", "int_0_20"), 
            ("utilization_rate", "pct"), ("default_status", "bool_20pct")
        ]
    },
    "9": {
        "name": "Fraud Detection",
        "columns": [
            ("transaction_id", "id"), ("source_account", "iban"), 
            ("amount_usd", "float_5_50000"), ("ip_address", "ipv4"), 
            ("device_fingerprint", "uuid"), ("is_fraud", "bool_5pct")
        ]
    },
    "10": {
        "name": "E-commerce Retail",
        "columns": [
            ("order_id", "id"), ("customer_id", "id"), ("product_sku", "sku"), 
            ("category", "choice_['Electronics','Furniture','Clothing','Toys','Grocery']"), 
            ("purchase_amount", "float_5_2000"), ("coupon_applied", "bool_30pct")
        ]
    },
    "11": {
        "name": "Real Estate",
        "columns": [
            ("property_id", "id"), ("zip_code", "zip"), ("square_footage", "int_500_5000"), 
            ("num_bedrooms", "int_1_6"), ("year_built", "int_1950_2023"), 
            ("sale_price", "int_50000_2000000")
        ]
    },
    "12": {
        "name": "Supply Chain",
        "columns": [
            ("warehouse_id", "id"), ("sku_id", "sku"), ("current_stock", "int_0_500"), 
            ("reorder_point", "int_10_100"), ("lead_time_days", "int_1_30"), 
            ("defect_rate", "float_0_0.15")
        ]
    },
    "13": {
        "name": "Insurance Pricing",
        "columns": [
            ("policy_holder_id", "id"), ("vehicle_class", "choice_['Sedan','SUV','Truck','Motorcycle']"), 
            ("annual_mileage", "int_1000_30000"), ("past_claims_count", "int_0_10"), 
            ("telemetry_speeding_events", "int_0_100"), ("premium_amount", "float_50_500")
        ]
    },
    "14": {
        "name": "Cryptocurrency",
        "columns": [
            ("block_height", "int_1_1000000"), ("tx_hash", "hash"), 
            ("sender_address", "wallet"), ("receiver_address", "wallet"), 
            ("token_amount", "float_0.1_100"), ("gas_fee_paid", "float_0.0001_0.1")
        ]
    },
    "15": {
        "name": "Sentiment Analysis",
        "columns": [
            ("text_id", "id"), ("raw_text", "sentence"), 
            ("platform", "choice_['Twitter','Facebook','Reddit','Youtube']"), 
            ("character_count", "int_10_500"), 
            ("sentiment_label", "choice_['Positive','Negative','Neutral']"), 
            ("confidence_score", "float_0.5_1.0")
        ]
    },
    "16": {
        "name": "Web Clickstream",
        "columns": [
            ("session_id", "uuid"), ("user_cookie", "uuid"), ("page_url", "url"), 
            ("time_spent_seconds", "int_1_1200"), ("referrer_url", "url"), 
            ("is_conversion", "bool_10pct")
        ]
    },
    "17": {
        "name": "Customer Churn",
        "columns": [
            ("subscriber_id", "id"), ("tenure_months", "int_1_60"), 
            ("monthly_charges", "float_10_150"), ("support_tickets_opened", "int_0_20"), 
            ("last_login_days_ago", "int_0_365"), ("churned", "bool_30pct")
        ]
    },
    "18": {
        "name": "Ad Impression",
        "columns": [
            ("impression_id", "id"), ("campaign_id", "id"), 
            ("ad_placement", "choice_['Header','Sidebar','Footer','Pop-up']"), 
            ("viewer_age", "int_18_65"), ("bid_price_cpm", "float_0.5_20.0"), 
            ("clicked", "bool_2pct")
        ]
    },
    "19": {
        "name": "Influencer Marketing",
        "columns": [
            ("influencer_handle", "handle"), ("follower_count", "int_1000_10000000"), 
            ("avg_likes_per_post", "int_10_50000"), ("sponsored_post_cost", "float_50_50000"), 
            ("engagement_rate", "float_0_0.20"), 
            ("niche_category", "choice_['Fashion','Gaming','Food','Tech','Fitness']")
        ]
    },
    "20": {
        "name": "Weather & Climate",
        "columns": [
            ("station_id", "id"), ("reading_datetime", "datetime"), 
            ("temp_celsius", "float_-20_45"), ("wind_speed_mps", "float_0_30"), 
            ("humidity_pct", "pct"), ("precipitation_mm", "float_0_50")
        ]
    },
    "21": {
        "name": "Seismology",
        "columns": [
            ("event_id", "id"), ("epicenter_latitude", "float_-90_90"), 
            ("epicenter_longitude", "float_-180_180"), ("depth_km", "float_0_700"), 
            ("richter_magnitude", "float_0_10"), ("station_count", "int_1_500")
        ]
    },
    "22": {
        "name": "Oceanography",
        "columns": [
            ("buoy_id", "id"), ("sea_surface_temp", "float_-2_35"), 
            ("salinity_psu", "float_30_38"), ("wave_height_meters", "float_0_15"), 
            ("current_direction_deg", "int_0_360"), ("dissolved_oxygen_ppm", "float_0_15")
        ]
    },
    "23": {
        "name": "Agricultural Yield",
        "columns": [
            ("plot_id", "id"), ("crop_type", "choice_['Corn','Wheat','Soybean','Rice']"), 
            ("soil_nitrogen_level", "float_0_100"), ("irrigation_m3", "float_0_5000"), 
            ("ndvi_index", "float_-1_1"), ("harvest_yield_kg", "int_0_20000")
        ]
    },
    "24": {
        "name": "Air Quality",
        "columns": [
            ("sensor_loc", "city"), ("pm2_5_concentration", "float_0_500"), 
            ("co_level_ppm", "float_0_50"), ("no2_level_ppb", "float_0_200"), 
            ("aqi_score", "int_0_500"), 
            ("dominant_pollutant", "choice_['PM2.5','PM10','Ozone','NO2','CO']")
        ]
    },
    "25": {
        "name": "Forestry",
        "columns": [
            ("grid_cell_id", "id"), ("canopy_cover_pct", "pct"), 
            ("deforestation_status", "choice_['Intact','Degraded','Clear-cut']"), 
            ("estimated_biomass_tons", "float_0_500"), 
            ("tree_species_dominant", "choice_['Oak','Pine','Maple','Mahogany']"), 
            ("wildfire_risk_index", "int_0_10")
        ]
    },
    "26": {
        "name": "Census & Demographics",
        "columns": [
            ("household_id", "id"), ("state_fips", "int_1_99"), 
            ("total_occupants", "int_1_10"), ("median_household_income", "int_10000_250000"), 
            ("education_level_head", "choice_['High School','Associate','Bachelors','Masters','PhD']"), 
            ("employment_status", "choice_['Employed','Unemployed','Retired','Student']")
        ]
    },
    "27": {
        "name": "Smart City Traffic",
        "columns": [
            ("intersection_id", "id"), ("timestamp_hour", "datetime_hour"), 
            ("vehicle_count", "int_0_500"), ("avg_speed_kmh", "int_0_120"), 
            ("congestion_level", "choice_['Low','Medium','High']"), 
            ("traffic_light_cycle_sec", "int_30_180")
        ]
    },
    "28": {
        "name": "Criminal Justice",
        "columns": [
            ("incident_id", "id"), ("offense_type", "choice_['Theft','Assault','Vandalism','DUI','Burglary']"), 
            ("latitude", "float_-90_90"), ("longitude", "float_-180_180"), 
            ("response_time_min", "int_1_60"), ("arrest_made", "bool_40pct")
        ]
    },
    "29": {
        "name": "Public Education",
        "columns": [
            ("school_id", "id"), ("student_teacher_ratio", "int_10_35"), 
            ("free_lunch_pct", "pct"), ("standardized_math_avg", "int_200_800"), 
            ("graduation_rate", "pct"), ("annual_budget_per_pupil", "int_5000_20000")
        ]
    },
    "30": {
        "name": "Voting & Elections",
        "columns": [
            ("precinct_id", "id"), ("registered_voters", "int_100_10000"), 
            ("votes_cast_republican", "int_0_5000"), ("votes_cast_democrat", "int_0_5000"), 
            ("absentee_ballots_count", "int_0_1000"), ("spoiled_ballots", "int_0_100")
        ]
    },
    "31": {
        "name": "Smart Grid",
        "columns": [
            ("meter_id", "id"), ("timestamp_15min", "datetime"), 
            ("active_power_kwh", "float_0_20"), ("reactive_power_kvarh", "float_0_10"), 
            ("voltage_level", "float_200_250"), ("peak_demand_flag", "bool_10pct")
        ]
    },
    "32": {
        "name": "Renewable Energy",
        "columns": [
            ("turbine_id", "id"), ("wind_speed_hub_height", "float_0_30"), 
            ("rotor_speed_rpm", "float_0_20"), ("blade_pitch_angle", "int_0_35"), 
            ("power_output_kw", "float_0_2000"), 
            ("maintenance_status", "choice_['Operational','Under Repair','Offline']")
        ]
    },
    "33": {
        "name": "Oil & Gas",
        "columns": [
            ("well_id", "id"), ("drilling_depth_meters", "float_0_10000"), 
            ("mud_weight_ppg", "float_8_16"), ("formation_pressure_psi", "float_0_10000"), 
            ("flow_rate_barrels_day", "float_0_5000"), ("gas_oil_ratio", "int_0_1000")
        ]
    },
    "34": {
        "name": "Water Management",
        "columns": [
            ("reservoir_id", "id"), ("water_level_meters", "float_0_100"), 
            ("daily_outflow_m3", "float_0_50000"), ("turbidity_ntu", "float_0_1000"), 
            ("ph_level", "float_0_14"), ("leakage_detected_m3", "float_0_500")
        ]
    },
    "35": {
        "name": "Streaming Media",
        "columns": [
            ("user_id", "id"), ("content_id", "id"), ("watch_duration_sec", "int_0_10000"), 
            ("device_type", "choice_['Mobile','Tablet','Desktop','TV']"), 
            ("completion_percentage", "pct"), ("rating_given", "int_0_5")
        ]
    },
    "36": {
        "name": "Sports Analytics",
        "columns": [
            ("player_id", "id"), ("game_id", "id"), ("minutes_played", "int_0_48"), 
            ("points_scored", "int_0_50"), ("sprint_distance_meters", "int_0_500"), 
            ("injury_risk_index", "float_0_1")
        ]
    },
    "37": {
        "name": "Music & Audio",
        "columns": [
            ("track_id", "id"), ("tempo_bpm", "int_60_200"), 
            ("spectral_centroid", "float_0_5000"), ("danceability_score", "float_0_1"), 
            ("loudness_db", "float_-30_0"), 
            ("genre_label", "choice_['Pop','Rock','Hip-Hop','Electronic','Jazz']")
        ]
    },
    "38": {
        "name": "Gaming Telemetry",
        "columns": [
            ("player_uuid", "uuid"), ("match_id", "uuid"), 
            ("character_class", "choice_['Warrior','Mage','Archer','Assassin','Healer']"), 
            ("kill_death_ratio", "float_0_5"), ("ping_ms", "int_10_250"), 
            ("session_duration_min", "int_1_240")
        ]
    },
    "39": {
        "name": "Server Logs",
        "columns": [
            ("log_timestamp", "datetime"), ("server_ip", "ipv4"), 
            ("cpu_utilization_pct", "pct"), ("ram_used_gb", "float_0_64"), 
            ("network_bytes_in", "int_0_1000000000"), 
            ("http_status_code", "choice_['200','301','404','500','502']")
        ]
    },
    "40": {
        "name": "Cybersecurity",
        "columns": [
            ("packet_id", "id"), ("source_port", "int_1_65535"), 
            ("dest_port", "int_1_65535"), ("payload_size_bytes", "int_0_1500"), 
            ("malware_signature_match", "bool_2pct"), ("threat_severity", "choice_['Low','Medium','High','Critical']")
        ]
    },
    "41": {
        "name": "Autonomous Driving",
        "columns": [
            ("frame_id", "id"), ("lidar_points_count", "int_0_500000"), 
            ("object_detected_class", "choice_['Car','Pedestrian','Cyclist','Traffic Sign','None']"), 
            ("distance_to_object_m", "float_0_200"), ("steering_angle_deg", "int_-45_45"), 
            ("throttle_pressure_pct", "pct")
        ]
    },
    "42": {
        "name": "Industrial IoT",
        "columns": [
            ("machine_id", "id"), ("vibration_frequency_hz", "float_0_500"), 
            ("bearing_temperature_c", "float_20_120"), ("cycles_completed", "int_0_1000000"), 
            ("oil_viscosity_cst", "float_10_100"), ("breakdown_predicted", "bool_5pct")
        ]
    },
    "43": {
        "name": "Robotics",
        "columns": [
            ("joint_id", "id"), ("target_position_rad", "float_-3.14_3.14"), 
            ("actual_position_rad", "float_-3.14_3.14"), ("motor_current_amperes", "float_0_50"), 
            ("end_effector_force_n", "float_0_1000"), ("trajectory_error", "float_0_0.5")
        ]
    },
    "44": {
        "name": "Ride-Hailing",
        "columns": [
            ("trip_id", "id"), ("pickup_geohash", "geohash"), 
            ("dropoff_geohash", "geohash"), ("surge_multiplier", "float_1.0_3.0"), 
            ("driver_rating", "float_0_5"), ("estimated_vs_actual_time_delta", "int_-30_60")
        ]
    },
    "45": {
        "name": "Aviation",
        "columns": [
            ("flight_number", "flight"), ("aircraft_tail_number", "tail"), 
            ("departure_delay_min", "int_0_300"), ("fuel_burn_rate_gph", "float_0_1000"), 
            ("altitude_ft", "int_0_45000"), ("air_turbulence_index", "float_0_3")
        ]
    },
    "46": {
        "name": "Maritime Freight",
        "columns": [
            ("vessel_mmsi", "id"), ("imo_number", "int_1000000_9999999"), 
            ("container_teu_load", "int_0_10000"), 
            ("destination_port_id", "choice_['ROT','LAX','SIN','HAM','NYK']"), 
            ("estimated_time_arrival", "date_future"), ("draft_depth_meters", "float_5_20")
        ]
    },
    "47": {
        "name": "Linguistics",
        "columns": [
            ("corpus_id", "id"), ("sentence_text", "sentence"), 
            ("pos_tags", "pos"), ("dependency_tree_depth", "int_1_20"), 
            ("language_iso_code", "choice_['en','es','fr','de','zh','ar']"), 
            ("word_count", "int_5_100")
        ]
    },
    "48": {
        "name": "Astronomy",
        "columns": [
            ("object_id", "id"), ("right_ascension_deg", "float_0_360"), 
            ("declination_deg", "float_-90_90"), ("apparent_magnitude", "float_-30_30"), 
            ("redshift_value", "float_0_10"), ("spectral_type", "choice_['O','B','A','F','G','K','M']")
        ]
    },
    "49": {
        "name": "Particle Physics",
        "columns": [
            ("collision_event_id", "id"), ("total_energy_gev", "float_0_14000"), 
            ("muon_track_count", "int_0_20"), ("missing_transverse_energy", "float_0_1000"), 
            ("invariant_mass_gev", "float_0_300"), ("is_higgs_boson_signature", "bool_1pct")
        ]
    },
    "50": {
        "name": "Historical Archives",
        "columns": [
            ("artifact_id", "id"), ("estimated_creation_century", "int_-3000_1900"), 
            ("origin_culture_civilization", "choice_['Egyptian','Roman','Greek','Mesopotamian','Indus Valley']"), 
            ("material_composition", "choice_['Bronze','Papyrus','Stone','Clay','Wood']"), 
            ("preservation_state_grade", "choice_['Poor','Fair','Good','Excellent']"), 
            ("digitized_text_transcription", "sentence")
        ]
    }
}

# --- HELPER FUNCTIONS TO GENERATE DATA ---

def generate_value(data_type):
    if data_type == "id":
        # This is a placeholder. The actual zero-padding happens in the main loop!
        return 0 
    elif data_type == "date_2024":
        return fake.date_between(start_date=datetime(2024,1,1), end_date=datetime(2026,12,31)).strftime("%Y-%m-%d")
    elif data_type == "date_week":
        return f"{fake.year()}-W{str(random.randint(1,52)).zfill(2)}"
    elif data_type == "datetime":
        return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    elif data_type == "datetime_hour":
        return f"2026-07-17 {str(random.randint(0,23)).zfill(2)}:00:00"
    elif data_type == "date_future":
        return fake.date_between(start_date=datetime.now(), end_date=datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
    elif data_type == "bp_sys":
        return random.randint(90, 180)
    elif data_type == "bp_dia":
        return random.randint(60, 120)
    elif data_type == "float_50_200":
        return round(random.uniform(50, 200), 2)
    elif data_type == "float_0.1_1.5":
        return round(random.uniform(0.1, 1.5), 3)
    elif data_type == "int_1_250000000":
        return random.randint(1, 250000000)
    elif "choice_" in data_type:
        options = data_type.replace("choice_", "").strip("[]").replace("'", "").split(",")
        return random.choice([opt.strip() for opt in options])
    elif data_type == "bbox":
        return f"[{random.randint(0,500)}, {random.randint(0,500)}, {random.randint(10,200)}, {random.randint(10,200)}]"
    elif data_type == "int_5_1000":
        return random.randint(5, 1000)
    elif data_type == "adverse":
        return random.choice(["Headache", "Nausea", "Dizziness", "Fatigue", "Rash", "Insomnia", "Hypertension"])
    elif data_type == "int_1_5":
        return random.randint(1, 5)
    elif data_type == "region":
        return f"REG-{fake.state_abbr()}{random.randint(10,99)}"
    elif data_type == "int_0_5000":
        return random.randint(0, 5000)
    elif data_type == "pct":
        return round(random.uniform(0, 100), 2)
    elif data_type == "int_0_500":
        return random.randint(0, 500)
    elif data_type == "int_40_180":
        return random.randint(40, 180)
    elif data_type == "int_0_15000":
        return random.randint(0, 15000)
    elif data_type == "int_50_1000":
        return random.randint(50, 1000)
    elif data_type == "ticker":
        return fake.word().upper()[:4]
    elif data_type == "float_10_500":
        return round(random.uniform(10, 500), 2)
    elif data_type == "int_1000_10000000":
        return random.randint(1000, 10000000)
    elif data_type == "int_20000_250000":
        return random.randint(20000, 250000)
    elif data_type == "float_0_1":
        return round(random.uniform(0, 1), 4)
    elif data_type == "int_0_20":
        return random.randint(0, 20)
    elif data_type == "float_5_50000":
        return round(random.uniform(5, 50000), 2)
    elif data_type == "iban":
        return fake.iban()
    elif data_type == "ipv4":
        return fake.ipv4()
    elif data_type == "uuid":
        return fake.uuid4()
    elif data_type == "sku":
        return f"SKU-{fake.word().upper()[:3]}{random.randint(100,999)}"
    elif data_type == "zip":
        return fake.zipcode()
    elif data_type == "int_500_5000":
        return random.randint(500, 5000)
    elif data_type == "int_1_6":
        return random.randint(1, 6)
    elif data_type == "int_1950_2023":
        return random.randint(1950, 2023)
    elif data_type == "int_50000_2000000":
        return random.randint(50000, 2000000)
    elif data_type == "int_0_500":
        return random.randint(0, 500)
    elif data_type == "int_10_100":
        return random.randint(10, 100)
    elif data_type == "int_1_30":
        return random.randint(1, 30)
    elif data_type == "float_0_0.15":
        return round(random.uniform(0, 0.15), 4)
    elif data_type == "int_1000_30000":
        return random.randint(1000, 30000)
    elif data_type == "int_0_10":
        return random.randint(0, 10)
    elif data_type == "int_0_100":
        return random.randint(0, 100)
    elif data_type == "float_50_500":
        return round(random.uniform(50, 500), 2)
    elif data_type == "int_1_1000000":
        return random.randint(1, 1000000)
    elif data_type == "hash":
        return fake.sha256()
    elif data_type == "wallet":
        return "0x" + fake.hexify(text="^"*40).upper()
    elif data_type == "float_0.1_100":
        return round(random.uniform(0.1, 100), 4)
    elif data_type == "float_0.0001_0.1":
        return round(random.uniform(0.0001, 0.1), 6)
    elif data_type == "sentence":
        return fake.sentence()
    elif data_type == "url":
        return fake.url()
    elif data_type == "int_1_1200":
        return random.randint(1, 1200)
    elif data_type == "int_1_60":
        return random.randint(1, 60)
    elif data_type == "float_10_150":
        return round(random.uniform(10, 150), 2)
    elif data_type == "int_0_365":
        return random.randint(0, 365)
    elif data_type == "int_18_65":
        return random.randint(18, 65)
    elif data_type == "float_0.5_20.0":
        return round(random.uniform(0.5, 20), 2)
    elif data_type == "handle":
        return "@" + fake.user_name()
    elif data_type == "int_1000_10000000":
        return random.randint(1000, 10000000)
    elif data_type == "int_10_50000":
        return random.randint(10, 50000)
    elif data_type == "float_50_50000":
        return round(random.uniform(50, 50000), 2)
    elif data_type == "float_0_0.20":
        return round(random.uniform(0, 0.20), 4)
    elif data_type == "float_-20_45":
        return round(random.uniform(-20, 45), 1)
    elif data_type == "float_0_30":
        return round(random.uniform(0, 30), 1)
    elif data_type == "float_0_50":
        return round(random.uniform(0, 50), 1)
    elif data_type == "float_-90_90":
        return round(random.uniform(-90, 90), 6)
    elif data_type == "float_-180_180":
        return round(random.uniform(-180, 180), 6)
    elif data_type == "float_0_700":
        return round(random.uniform(0, 700), 1)
    elif data_type == "float_0_10":
        return round(random.uniform(0, 10), 2)
    elif data_type == "int_1_500":
        return random.randint(1, 500)
    elif data_type == "float_-2_35":
        return round(random.uniform(-2, 35), 1)
    elif data_type == "float_30_38":
        return round(random.uniform(30, 38), 1)
    elif data_type == "float_0_15":
        return round(random.uniform(0, 15), 1)
    elif data_type == "int_0_360":
        return random.randint(0, 360)
    elif data_type == "float_0_15":
        return round(random.uniform(0, 15), 2)
    elif data_type == "float_0_100":
        return round(random.uniform(0, 100), 1)
    elif data_type == "float_0_5000":
        return round(random.uniform(0, 5000), 1)
    elif data_type == "float_-1_1":
        return round(random.uniform(-1, 1), 3)
    elif data_type == "int_0_20000":
        return random.randint(0, 20000)
    elif data_type == "city":
        return fake.city()
    elif data_type == "float_0_500":
        return round(random.uniform(0, 500), 2)
    elif data_type == "float_0_50":
        return round(random.uniform(0, 50), 1)
    elif data_type == "float_0_200":
        return round(random.uniform(0, 200), 1)
    elif data_type == "int_0_500":
        return random.randint(0, 500)
    elif data_type == "int_1_99":
        return random.randint(1, 99)
    elif data_type == "int_1_10":
        return random.randint(1, 10)
    elif data_type == "int_10000_250000":
        return random.randint(10000, 250000)
    elif data_type == "int_0_120":
        return random.randint(0, 120)
    elif data_type == "int_30_180":
        return random.randint(30, 180)
    elif data_type == "int_10_35":
        return random.randint(10, 35)
    elif data_type == "int_200_800":
        return random.randint(200, 800)
    elif data_type == "int_5000_20000":
        return random.randint(5000, 20000)
    elif data_type == "int_100_10000":
        return random.randint(100, 10000)
    elif data_type == "int_0_5000":
        return random.randint(0, 5000)
    elif data_type == "int_0_1000":
        return random.randint(0, 1000)
    elif data_type == "float_0_20":
        return round(random.uniform(0, 20), 2)
    elif data_type == "float_200_250":
        return round(random.uniform(200, 250), 1)
    elif data_type == "float_0_35":
        return int(random.uniform(0, 35))
    elif data_type == "float_0_2000":
        return round(random.uniform(0, 2000), 1)
    elif data_type == "float_0_10000":
        return round(random.uniform(0, 10000), 2)
    elif data_type == "float_8_16":
        return round(random.uniform(8, 16), 1)
    elif data_type == "int_0_1000":
        return random.randint(0, 1000)
    elif data_type == "float_0_100":
        return round(random.uniform(0, 100), 2)
    elif data_type == "float_0_50000":
        return round(random.uniform(0, 50000), 1)
    elif data_type == "float_0_1000":
        return round(random.uniform(0, 1000), 1)
    elif data_type == "float_0_14":
        return round(random.uniform(0, 14), 1)
    elif data_type == "int_0_10000":
        return random.randint(0, 10000)
    elif data_type == "int_0_48":
        return random.randint(0, 48)
    elif data_type == "int_0_50":
        return random.randint(0, 50)
    elif data_type == "int_0_500":
        return random.randint(0, 500)
    elif data_type == "int_60_200":
        return random.randint(60, 200)
    elif data_type == "float_0_5000":
        return round(random.uniform(0, 5000), 2)
    elif data_type == "float_-30_0":
        return round(random.uniform(-30, 0), 2)
    elif data_type == "int_10_250":
        return random.randint(10, 250)
    elif data_type == "int_1_240":
        return random.randint(1, 240)
    elif data_type == "float_0_64":
        return round(random.uniform(0, 64), 1)
    elif data_type == "int_0_1000000000":
        return random.randint(0, 1000000000)
    elif data_type == "int_1_65535":
        return random.randint(1, 65535)
    elif data_type == "int_0_1500":
        return random.randint(0, 1500)
    elif data_type == "int_0_500000":
        return random.randint(0, 500000)
    elif data_type == "float_0_200":
        return round(random.uniform(0, 200), 2)
    elif data_type == "int_-45_45":
        return random.randint(-45, 45)
    elif data_type == "float_0_500":
        return round(random.uniform(0, 500), 2)
    elif data_type == "int_20_120":
        return random.randint(20, 120)
    elif data_type == "int_0_1000000":
        return random.randint(0, 1000000)
    elif data_type == "float_10_100":
        return round(random.uniform(10, 100), 1)
    elif data_type == "float_-3.14_3.14":
        return round(random.uniform(-3.14, 3.14), 3)
    elif data_type == "float_0_50":
        return round(random.uniform(0, 50), 2)
    elif data_type == "float_0_1000":
        return round(random.uniform(0, 1000), 1)
    elif data_type == "float_0_0.5":
        return round(random.uniform(0, 0.5), 3)
    elif data_type == "geohash":
        return fake.word()[:7].lower()
    elif data_type == "float_1.0_3.0":
        return round(random.uniform(1.0, 3.0), 1)
    elif data_type == "float_0_5":
        return round(random.uniform(0, 5), 1)
    elif data_type == "int_-30_60":
        return random.randint(-30, 60)
    elif data_type == "flight":
        return f"{fake.airline()}{random.randint(10,9999)}"
    elif data_type == "tail":
        return f"N{random.randint(100,999)}AB"
    elif data_type == "int_0_300":
        return random.randint(0, 300)
    elif data_type == "float_0_1000":
        return round(random.uniform(0, 1000), 1)
    elif data_type == "int_0_45000":
        return random.randint(0, 45000)
    elif data_type == "float_0_3":
        return round(random.uniform(0, 3), 1)
    elif data_type == "int_1000000_9999999":
        return random.randint(1000000, 9999999)
    elif data_type == "int_0_10000":
        return random.randint(0, 10000)
    elif data_type == "float_5_20":
        return round(random.uniform(5, 20), 1)
    elif data_type == "pos":
        return f"{fake.word()}_{random.choice(['NOUN','VERB','ADJ','ADP','DET'])}"
    elif data_type == "int_1_20":
        return random.randint(1, 20)
    elif data_type == "int_5_100":
        return random.randint(5, 100)
    elif data_type == "float_0_360":
        return round(random.uniform(0, 360), 4)
    elif data_type == "float_-30_30":
        return round(random.uniform(-30, 30), 2)
    elif data_type == "float_0_10":
        return round(random.uniform(0, 10), 3)
    elif data_type == "float_0_14000":
        return round(random.uniform(0, 14000), 2)
    elif data_type == "int_0_20":
        return random.randint(0, 20)
    elif data_type == "float_0_1000":
        return round(random.uniform(0, 1000), 2)
    elif data_type == "float_0_300":
        return round(random.uniform(0, 300), 2)
    elif data_type == "int_-3000_1900":
        return random.randint(-3000, 1900)
    elif data_type == "bool_1pct": return 1 if random.random() < 0.01 else 0
    elif data_type == "bool_2pct": return 1 if random.random() < 0.02 else 0
    elif data_type == "bool_5pct": return 1 if random.random() < 0.05 else 0
    elif data_type == "bool_10pct": return 1 if random.random() < 0.10 else 0
    elif data_type == "bool_20pct": return 1 if random.random() < 0.20 else 0
    elif data_type == "bool_30pct": return 1 if random.random() < 0.30 else 0
    elif data_type == "bool_40pct": return 1 if random.random() < 0.40 else 0
    
    return "MISSING"

# --- HELPER TO MAKE COLUMN NAMES NEAT & TITLE CASE ---
def format_column_name(col_name):
    # Convert snake_case to Title Case (e.g., patient_id -> Patient_Id)
    return col_name.replace("_", " ").title().replace(" ", "_")

# --- MAIN PROGRAM ---
def main():
    print("\n" + "="*60)
    print("     MASSIVE CSV DATASET GENERATOR (50 Categories)")
    print("="*60)
    
    # Step 1: Ask for the dataset
    print("\nAvailable Datasets:")
    for key, val in DATASETS.items():
        print(f"{key}. {val['name']}")
        
    while True:
        try:
            choice = input(f"\nEnter the Number of the dataset you want (1-50): ").strip()
            if choice in DATASETS:
                selected = DATASETS[choice]
                break
            else:
                print("Invalid number. Please enter a number between 1 and 50.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return

    print(f"\nSelected: {selected['name']}")

    # Step 2: Ask for number of rows
    while True:
        try:
            num_rows = int(input("\nHow many rows do you want to generate? (e.g., 5000, 10000): ").strip())
            if num_rows > 0:
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return

    # Step 3: Ask for filename
    filename = input("\nWhat should the CSV file be named? (e.g., 'medical_data'): ").strip()
    if not filename:
        filename = "dataset"
    if not filename.endswith(".csv"):
        filename += ".csv"

    # Step 4: Calculate ID padding based on row count
    # If user asks for 5000, we pad to 4 digits. If 10000, 5 digits, etc.
    id_padding = len(str(num_rows))

    # Step 5: Generate the Data
    print(f"\n↪ Generating {num_rows} rows of data... Please wait...")
    
    # Get columns and format them in Title Case
    cols = [format_column_name(col[0]) for col in selected['columns']]
    data = []

    for i in range(num_rows):
        row = []
        for col_name, dtype in selected['columns']:
            val = generate_value(dtype)
            
            # If the type is 'id', apply the zero-padding based on the user's row count
            if dtype == "id":
                # i is 0-based (0, 1, 2), so we add 1 to make it 1-based (1, 2, 3)
                val = str(i + 1).zfill(id_padding)
                
            row.append(val)
        data.append(row)

    # Step 6: Create DataFrame and save
    df = pd.DataFrame(data, columns=cols)
    
    try:
        df.to_csv(filename, index=False)
        full_path = os.path.abspath(filename)
        print(f"\n✅ SUCCESS! CSV file saved.")
        print(f"    File Name: {filename}")
        print(f"    Location: {full_path}")
        print(f"    Rows Generated: {num_rows}")
        print(f"    Dataset Type: {selected['name']}")
        print(f"    ID Format: 0-padded to {id_padding} digits (e.g., {str(1).zfill(id_padding)})")
    except Exception as e:
        print(f"\n❌ ERROR saving file: {e}")

if __name__ == "__main__":
    main()