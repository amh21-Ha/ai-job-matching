def score_technical(test_results: dict) -> float:
    # Example: weighted scoring
    coding = test_results.get("coding", 0)
    sql = test_results.get("sql", 0)
    ml = test_results.get("ml", 0)
    
    return round(0.5*coding + 0.3*sql + 0.2*ml, 2)

