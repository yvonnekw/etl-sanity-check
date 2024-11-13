import pytest
import pandas as pd


# test if there are any duplicate records/rows in target system
def test_check_duplicates():
    target_df = pd.read_csv("employee_dept_no_copy_tgt.csv", sep=",")
    count = target_df.duplicated().sum()
    assert count == 0, "Duplication found - please verify the target"


# test if target is not blank
def test_dat_completeness():
    target_df = pd.read_csv("employee_dept_no_copy_tgt.csv")
    assert not target_df.empty, "Target file is empty- please verify the ETL process"


# Test if deptno is a manadatory column
def test_deptno_for_null_value_check():
    target_df = pd.read_csv("employee_dept_no_copy_tgt.csv")
    isDeptNoNull = target_df['deptno'].isnull().any()
    assert isDeptNoNull == False, "Department no is contains a null value - Please check"


# Test if eno is always a primary key
def test_eno_for_unique_value_check():
    target_df = pd.read_csv("employee_dept_no_copy_tgt.csv")
    totalCount = target_df["eno"].count()
    deptNoUniqueValueCount = len(target_df["eno"].unique())
    assert totalCount == deptNoUniqueValueCount, "eno column values are not unique - please check"
