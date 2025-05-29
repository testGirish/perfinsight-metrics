def calculate_metrics(data):
    """Calculate performance metrics from raw data."""
    if not data:
        return None
        
    total = sum(data)
    average = total / len(data)
    
    return {
        'total': total,
        'average': average,
        'count': len(data)
    }
#Below is the analyze performance method.
def analyze_performance(metrics):
    """Analyze performance metrics."""
    if not metrics:
        return 'No data available'
        
    if metrics['average'] > 90:
        return 'Excellent'
    elif metrics['average'] > 70:
        return 'Good'
    else:
        return 'Needs improvement'

def main():
    test_data = [85, 92, 78, 95, 88]
    metrics = calculate_metrics(test_data)
    result = analyze_performance(metrics)
    print(f"Performance Analysis: {result}")

if __name__ == '__main__':
    main()
