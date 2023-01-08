"Define temp-table tt-organizations no-undo
	field id as integer no-undo
	field organizationName as character no-undo
	field organizationOID as character no-undo
	field id as character no-undo
index organizations-id as primary as unique id."
"Define temp-table tt-alternateUnitIDs no-undo
	field id as integer no-undo
	field id_1 as character no-undo
	field name as character no-undo
index alternateUnitIDs-id as primary as unique id."
"Define temp-table tt-governmentRegistrations no-undo
	field id as integer no-undo
	field registeredName as character no-undo
	field cityName as character no-undo
	field countryCode as character no-undo
	field formattedAddress as character no-undo
	field lineOne as character no-undo
	field lineThree as character no-undo
	field lineTwo as character no-undo
	field postalCode as character no-undo
	field contactID as character no-undo
	field number as character no-undo
	field effectiveDateTime as character no-undo
	field code_2 as character no-undo
	field name_2 as character no-undo
	field subdivisionType as character no-undo
	field familyName as character no-undo
	field formattedName as character no-undo
	field givenName as character no-undo
	field middleName as character no-undo
	field code as character no-undo
	field name_1 as character no-undo
index governmentRegistrations-id as primary as unique id."
"Define temp-table tt-industryClassifications no-undo
	field id as integer no-undo
	field code_3 as character no-undo
	field name_4 as character no-undo
	field name_3 as character no-undo
index industryClassifications-id as primary as unique id."
"Define temp-table tt-emails no-undo
	field id as integer no-undo
	field emailUri as character no-undo
index emails-id as primary as unique id."
"Define temp-table tt-telephones no-undo
	field id as integer no-undo
	field areaDialing as character no-undo
	field dialNumber as character no-undo
	field formattedNumber as character no-undo
	field teste as character no-undo
index telephones-id as primary as unique id."
