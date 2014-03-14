class ModelsMap:
	Map = [
		{
			'name': 'user',
			'repr': 'User',
			'properties': [
				{'name': 'name'		, 'repr': 'Name'	, 'type': 'text'	, 'data': '' },
				{'name': 'pw_hash'	, 'repr': 'Hash' 	, 'type': 'text'	, 'data': '' }
			],
			'references': [
				{'name': 'expenses', 'repr': 'Expenses', 'kind': 'Expense', 'repeated': 'True'}
			]
		},
		{
			'name': 'expense',
			'repr': 'Expense',
			'properties': [
				{'name': 'amount'		, 'repr': 'Amount'		, 'type': 'number'	, 'data': '' },
				{'name': 'category'		, 'repr': 'Category'	, 'type': 'text'	, 'data': '' },
				{'name': 'description'	, 'repr': 'Description'	, 'type': 'text'	, 'data': '' }
			],
			'references': [
				{'name': 'userKey', 'repr': 'Users', 'kind': 'User', 'repeated': 'False'}
			]
		}
	]