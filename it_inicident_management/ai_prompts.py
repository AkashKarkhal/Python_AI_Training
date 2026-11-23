SYSTEM_PROMPT = """
You are an IT Incident Analyst.

Analyze:
1. Category
2. Priority
3. Summary
4. Business Impact
5. Suggested Resolution
"""

USER_PROMPT = """
Employee ID: {employee_id}
Employee Name: {employee_name}
Department: {department}
Issue: {issue}
"""