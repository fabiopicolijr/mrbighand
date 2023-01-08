"Define temp-table tt-payrollScheduleUploads no-undo
	field id as integer no-undo
	field nome as character no-undo
	field uploadID as character no-undo
	field number as integer no-undo
index payrollScheduleUploads-id as primary as unique id."
"Define temp-table tt-payrollSchedules no-undo
	field id as integer no-undo
	field payPeriodEndDate as character no-undo
	field uploadID__1 as character no-undo
index payrollSchedules-id as primary as unique id."
