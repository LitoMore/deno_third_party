ADS_ATTR_CLEAR = ( 1 )
ADS_ATTR_UPDATE = ( 2 )
ADS_ATTR_APPEND = ( 3 )
ADS_ATTR_DELETE = ( 4 )
ADS_EXT_MINEXTDISPID = ( 1 )
ADS_EXT_MAXEXTDISPID = ( 16777215 )
ADS_EXT_INITCREDENTIALS = ( 1 )
ADS_EXT_INITIALIZE_COMPLETE = ( 2 )

ADS_SEARCHPREF_ASYNCHRONOUS     = 0
ADS_SEARCHPREF_DEREF_ALIASES    = 1
ADS_SEARCHPREF_SIZE_LIMIT       = 2
ADS_SEARCHPREF_TIME_LIMIT       = 3
ADS_SEARCHPREF_ATTRIBTYPES_ONLY = 4
ADS_SEARCHPREF_SEARCH_SCOPE     = 5
ADS_SEARCHPREF_TIMEOUT          = 6
ADS_SEARCHPREF_PAGESIZE         = 7
ADS_SEARCHPREF_PAGED_TIME_LIMIT = 8
ADS_SEARCHPREF_CHASE_REFERRALS  = 9
ADS_SEARCHPREF_SORT_ON          = 10
ADS_SEARCHPREF_CACHE_RESULTS    = 11
ADS_SEARCHPREF_DIRSYNC          = 12
ADS_SEARCHPREF_TOMBSTONE        = 13

ADS_SCOPE_BASE        = 0
ADS_SCOPE_ONELEVEL    = 1
ADS_SCOPE_SUBTREE     = 2

ADS_SECURE_AUTHENTICATION  = 0x1
ADS_USE_ENCRYPTION         = 0x2
ADS_USE_SSL                = 0x2
ADS_READONLY_SERVER        = 0x4
ADS_PROMPT_CREDENTIALS     = 0x8
ADS_NO_AUTHENTICATION      = 0x10
ADS_FAST_BIND              = 0x20
ADS_USE_SIGNING            = 0x40
ADS_USE_SEALING            = 0x80
ADS_USE_DELEGATION         = 0x100
ADS_SERVER_BIND            = 0x200

ADSTYPE_INVALID	= 0
ADSTYPE_DN_STRING	= ADSTYPE_INVALID + 1
ADSTYPE_CASE_EXACT_STRING	= ADSTYPE_DN_STRING + 1
ADSTYPE_CASE_IGNORE_STRING	= ADSTYPE_CASE_EXACT_STRING + 1
ADSTYPE_PRINTABLE_STRING	= ADSTYPE_CASE_IGNORE_STRING + 1
ADSTYPE_NUMERIC_STRING	= ADSTYPE_PRINTABLE_STRING + 1
ADSTYPE_BOOLEAN	= ADSTYPE_NUMERIC_STRING + 1
ADSTYPE_INTEGER	= ADSTYPE_BOOLEAN + 1
ADSTYPE_OCTET_STRING	= ADSTYPE_INTEGER + 1
ADSTYPE_UTC_TIME	= ADSTYPE_OCTET_STRING + 1
ADSTYPE_LARGE_INTEGER	= ADSTYPE_UTC_TIME + 1
ADSTYPE_PROV_SPECIFIC	= ADSTYPE_LARGE_INTEGER + 1
ADSTYPE_OBJECT_CLASS	= ADSTYPE_PROV_SPECIFIC + 1
ADSTYPE_CASEIGNORE_LIST	= ADSTYPE_OBJECT_CLASS + 1
ADSTYPE_OCTET_LIST	= ADSTYPE_CASEIGNORE_LIST + 1
ADSTYPE_PATH	= ADSTYPE_OCTET_LIST + 1
ADSTYPE_POSTALADDRESS	= ADSTYPE_PATH + 1
ADSTYPE_TIMESTAMP	= ADSTYPE_POSTALADDRESS + 1
ADSTYPE_BACKLINK	= ADSTYPE_TIMESTAMP + 1
ADSTYPE_TYPEDNAME	= ADSTYPE_BACKLINK + 1
ADSTYPE_HOLD	= ADSTYPE_TYPEDNAME + 1
ADSTYPE_NETADDRESS	= ADSTYPE_HOLD + 1
ADSTYPE_REPLICAPOINTER	= ADSTYPE_NETADDRESS + 1
ADSTYPE_FAXNUMBER	= ADSTYPE_REPLICAPOINTER + 1
ADSTYPE_EMAIL	= ADSTYPE_FAXNUMBER + 1
ADSTYPE_NT_SECURITY_DESCRIPTOR	= ADSTYPE_EMAIL + 1
ADSTYPE_UNKNOWN	= ADSTYPE_NT_SECURITY_DESCRIPTOR + 1
ADSTYPE_DN_WITH_BINARY	= ADSTYPE_UNKNOWN + 1
ADSTYPE_DN_WITH_STRING	= ADSTYPE_DN_WITH_BINARY + 1

ADS_PROPERTY_CLEAR	= 1
ADS_PROPERTY_UPDATE	= 2
ADS_PROPERTY_APPEND	= 3
ADS_PROPERTY_DELETE	= 4
ADS_SYSTEMFLAG_DISALLOW_DELETE	= -2147483648
ADS_SYSTEMFLAG_CONFIG_ALLOW_RENAME	= 0x40000000
ADS_SYSTEMFLAG_CONFIG_ALLOW_MOVE	= 0x20000000
ADS_SYSTEMFLAG_CONFIG_ALLOW_LIMITED_MOVE	= 0x10000000
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_RENAME	= -2147483648
ADS_SYSTEMFLAG_DOMAIN_DISALLOW_MOVE	= 0x4000000
ADS_SYSTEMFLAG_CR_NTDS_NC	= 0x1
ADS_SYSTEMFLAG_CR_NTDS_DOMAIN	= 0x2
ADS_SYSTEMFLAG_ATTR_NOT_REPLICATED	= 0x1
ADS_SYSTEMFLAG_ATTR_IS_CONSTRUCTED	= 0x4
ADS_GROUP_TYPE_GLOBAL_GROUP	= 0x2
ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP	= 0x4
ADS_GROUP_TYPE_LOCAL_GROUP	= 0x4
ADS_GROUP_TYPE_UNIVERSAL_GROUP	= 0x8
ADS_GROUP_TYPE_SECURITY_ENABLED	= -2147483648
ADS_UF_SCRIPT	= 0x1
ADS_UF_ACCOUNTDISABLE	= 0x2
ADS_UF_HOMEDIR_REQUIRED	= 0x8
ADS_UF_LOCKOUT	= 0x10
ADS_UF_PASSWD_NOTREQD	= 0x20
ADS_UF_PASSWD_CANT_CHANGE	= 0x40
ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED	= 0x80
ADS_UF_TEMP_DUPLICATE_ACCOUNT	= 0x100
ADS_UF_NORMAL_ACCOUNT	= 0x200
ADS_UF_INTERDOMAIN_TRUST_ACCOUNT	= 0x800
ADS_UF_WORKSTATION_TRUST_ACCOUNT	= 0x1000
ADS_UF_SERVER_TRUST_ACCOUNT	= 0x2000
ADS_UF_DONT_EXPIRE_PASSWD	= 0x10000
ADS_UF_MNS_LOGON_ACCOUNT	= 0x20000
ADS_UF_SMARTCARD_REQUIRED	= 0x40000
ADS_UF_TRUSTED_FOR_DELEGATION	= 0x80000
ADS_UF_NOT_DELEGATED	= 0x100000
ADS_UF_USE_DES_KEY_ONLY	= 0x200000
ADS_UF_DONT_REQUIRE_PREAUTH	= 0x400000
ADS_UF_PASSWORD_EXPIRED	= 0x800000
ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION	= 0x1000000
ADS_RIGHT_DELETE	= 0x10000
ADS_RIGHT_READ_CONTROL	= 0x20000
ADS_RIGHT_WRITE_DAC	= 0x40000
ADS_RIGHT_WRITE_OWNER	= 0x80000
ADS_RIGHT_SYNCHRONIZE	= 0x100000
ADS_RIGHT_ACCESS_SYSTEM_SECURITY	= 0x1000000
ADS_RIGHT_GENERIC_READ	= -2147483648
ADS_RIGHT_GENERIC_WRITE	= 0x40000000
ADS_RIGHT_GENERIC_EXECUTE	= 0x20000000
ADS_RIGHT_GENERIC_ALL	= 0x10000000
ADS_RIGHT_DS_CREATE_CHILD	= 0x1
ADS_RIGHT_DS_DELETE_CHILD	= 0x2
ADS_RIGHT_ACTRL_DS_LIST	= 0x4
ADS_RIGHT_DS_SELF	= 0x8
ADS_RIGHT_DS_READ_PROP	= 0x10
ADS_RIGHT_DS_WRITE_PROP	= 0x20
ADS_RIGHT_DS_DELETE_TREE	= 0x40
ADS_RIGHT_DS_LIST_OBJECT	= 0x80
ADS_RIGHT_DS_CONTROL_ACCESS	= 0x100
ADS_ACETYPE_ACCESS_ALLOWED	= 0
ADS_ACETYPE_ACCESS_DENIED	= 0x1
ADS_ACETYPE_SYSTEM_AUDIT	= 0x2
ADS_ACETYPE_ACCESS_ALLOWED_OBJECT	= 0x5
ADS_ACETYPE_ACCESS_DENIED_OBJECT	= 0x6
ADS_ACETYPE_SYSTEM_AUDIT_OBJECT	= 0x7
ADS_ACETYPE_SYSTEM_ALARM_OBJECT	= 0x8
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK	= 0x9
ADS_ACETYPE_ACCESS_DENIED_CALLBACK	= 0xa
ADS_ACETYPE_ACCESS_ALLOWED_CALLBACK_OBJECT	= 0xb
ADS_ACETYPE_ACCESS_DENIED_CALLBACK_OBJECT	= 0xc
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK	= 0xd
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK	= 0xe
ADS_ACETYPE_SYSTEM_AUDIT_CALLBACK_OBJECT	= 0xf
ADS_ACETYPE_SYSTEM_ALARM_CALLBACK_OBJECT	= 0x10
ADS_ACEFLAG_INHERIT_ACE	= 0x2
ADS_ACEFLAG_NO_PROPAGATE_INHERIT_ACE	= 0x4
ADS_ACEFLAG_INHERIT_ONLY_ACE	= 0x8
ADS_ACEFLAG_INHERITED_ACE	= 0x10
ADS_ACEFLAG_VALID_INHERIT_FLAGS	= 0x1f
ADS_ACEFLAG_SUCCESSFUL_ACCESS	= 0x40
ADS_ACEFLAG_FAILED_ACCESS	= 0x80
ADS_FLAG_OBJECT_TYPE_PRESENT	= 0x1
ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT	= 0x2
ADS_SD_CONTROL_SE_OWNER_DEFAULTED	= 0x1
ADS_SD_CONTROL_SE_GROUP_DEFAULTED	= 0x2
ADS_SD_CONTROL_SE_DACL_PRESENT	= 0x4
ADS_SD_CONTROL_SE_DACL_DEFAULTED	= 0x8
ADS_SD_CONTROL_SE_SACL_PRESENT	= 0x10
ADS_SD_CONTROL_SE_SACL_DEFAULTED	= 0x20
ADS_SD_CONTROL_SE_DACL_AUTO_INHERIT_REQ	= 0x100
ADS_SD_CONTROL_SE_SACL_AUTO_INHERIT_REQ	= 0x200
ADS_SD_CONTROL_SE_DACL_AUTO_INHERITED	= 0x400
ADS_SD_CONTROL_SE_SACL_AUTO_INHERITED	= 0x800
ADS_SD_CONTROL_SE_DACL_PROTECTED	= 0x1000
ADS_SD_CONTROL_SE_SACL_PROTECTED	= 0x2000
ADS_SD_CONTROL_SE_SELF_RELATIVE	= 0x8000
ADS_SD_REVISION_DS	= 4
ADS_NAME_TYPE_1779	= 1
ADS_NAME_TYPE_CANONICAL	= 2
ADS_NAME_TYPE_NT4	= 3
ADS_NAME_TYPE_DISPLAY	= 4
ADS_NAME_TYPE_DOMAIN_SIMPLE	= 5
ADS_NAME_TYPE_ENTERPRISE_SIMPLE	= 6
ADS_NAME_TYPE_GUID	= 7
ADS_NAME_TYPE_UNKNOWN	= 8
ADS_NAME_TYPE_USER_PRINCIPAL_NAME	= 9
ADS_NAME_TYPE_CANONICAL_EX	= 10
ADS_NAME_TYPE_SERVICE_PRINCIPAL_NAME	= 11
ADS_NAME_TYPE_SID_OR_SID_HISTORY_NAME	= 12
ADS_NAME_INITTYPE_DOMAIN	= 1
ADS_NAME_INITTYPE_SERVER	= 2
ADS_NAME_INITTYPE_GC	= 3
ADS_OPTION_SERVERNAME	= 0
ADS_OPTION_REFERRALS	= ADS_OPTION_SERVERNAME + 1
ADS_OPTION_PAGE_SIZE	= ADS_OPTION_REFERRALS + 1
ADS_OPTION_SECURITY_MASK	= ADS_OPTION_PAGE_SIZE + 1
ADS_OPTION_MUTUAL_AUTH_STATUS	= ADS_OPTION_SECURITY_MASK + 1
ADS_OPTION_QUOTA	= ADS_OPTION_MUTUAL_AUTH_STATUS + 1
ADS_OPTION_PASSWORD_PORTNUMBER	= ADS_OPTION_QUOTA + 1
ADS_OPTION_PASSWORD_METHOD	= ADS_OPTION_PASSWORD_PORTNUMBER + 1
ADS_SECURITY_INFO_OWNER	= 0x1
ADS_SECURITY_INFO_GROUP	= 0x2
ADS_SECURITY_INFO_DACL	= 0x4
ADS_SECURITY_INFO_SACL	= 0x8
ADS_SETTYPE_FULL	= 1
ADS_SETTYPE_PROVIDER	= 2
ADS_SETTYPE_SERVER	= 3
ADS_SETTYPE_DN	= 4
ADS_FORMAT_WINDOWS	= 1
ADS_FORMAT_WINDOWS_NO_SERVER	= 2
ADS_FORMAT_WINDOWS_DN	= 3
ADS_FORMAT_WINDOWS_PARENT	= 4
ADS_FORMAT_X500	= 5
ADS_FORMAT_X500_NO_SERVER	= 6
ADS_FORMAT_X500_DN	= 7
ADS_FORMAT_X500_PARENT	= 8
ADS_FORMAT_SERVER	= 9
ADS_FORMAT_PROVIDER	= 10
ADS_FORMAT_LEAF	= 11
ADS_DISPLAY_FULL	= 1
ADS_DISPLAY_VALUE_ONLY	= 2
ADS_ESCAPEDMODE_DEFAULT	= 1
ADS_ESCAPEDMODE_ON	= 2
ADS_ESCAPEDMODE_OFF	= 3
ADS_ESCAPEDMODE_OFF_EX	= 4
ADS_PATH_FILE	= 1
ADS_PATH_FILESHARE	= 2
ADS_PATH_REGISTRY	= 3
ADS_SD_FORMAT_IID	= 1
ADS_SD_FORMAT_RAW	= 2
ADS_SD_FORMAT_HEXSTRING	= 3


# Generated by h2py from AdsErr.h
def _HRESULT_TYPEDEF_(_sc): return _sc

E_ADS_BAD_PATHNAME = _HRESULT_TYPEDEF_((-2147463168))
E_ADS_INVALID_DOMAIN_OBJECT = _HRESULT_TYPEDEF_((-2147463167))
E_ADS_INVALID_USER_OBJECT = _HRESULT_TYPEDEF_((-2147463166))
E_ADS_INVALID_COMPUTER_OBJECT = _HRESULT_TYPEDEF_((-2147463165))
E_ADS_UNKNOWN_OBJECT = _HRESULT_TYPEDEF_((-2147463164))
E_ADS_PROPERTY_NOT_SET = _HRESULT_TYPEDEF_((-2147463163))
E_ADS_PROPERTY_NOT_SUPPORTED = _HRESULT_TYPEDEF_((-2147463162))
E_ADS_PROPERTY_INVALID = _HRESULT_TYPEDEF_((-2147463161))
E_ADS_BAD_PARAMETER = _HRESULT_TYPEDEF_((-2147463160))
E_ADS_OBJECT_UNBOUND = _HRESULT_TYPEDEF_((-2147463159))
E_ADS_PROPERTY_NOT_MODIFIED = _HRESULT_TYPEDEF_((-2147463158))
E_ADS_PROPERTY_MODIFIED = _HRESULT_TYPEDEF_((-2147463157))
E_ADS_CANT_CONVERT_DATATYPE = _HRESULT_TYPEDEF_((-2147463156))
E_ADS_PROPERTY_NOT_FOUND = _HRESULT_TYPEDEF_((-2147463155))
E_ADS_OBJECT_EXISTS = _HRESULT_TYPEDEF_((-2147463154))
E_ADS_SCHEMA_VIOLATION = _HRESULT_TYPEDEF_((-2147463153))
E_ADS_COLUMN_NOT_SET = _HRESULT_TYPEDEF_((-2147463152))
S_ADS_ERRORSOCCURRED = _HRESULT_TYPEDEF_(0x00005011)
S_ADS_NOMORE_ROWS = _HRESULT_TYPEDEF_(0x00005012)
S_ADS_NOMORE_COLUMNS = _HRESULT_TYPEDEF_(0x00005013)
E_ADS_INVALID_FILTER = _HRESULT_TYPEDEF_((-2147463148))

# ADS_DEREFENUM enum
ADS_DEREF_NEVER	= 0
ADS_DEREF_SEARCHING	= 1
ADS_DEREF_FINDING	= 2
ADS_DEREF_ALWAYS	= 3

# ADS_PREFERENCES_ENUM
ADSIPROP_ASYNCHRONOUS	= 0
ADSIPROP_DEREF_ALIASES	= 0x1
ADSIPROP_SIZE_LIMIT	= 0x2
ADSIPROP_TIME_LIMIT	= 0x3
ADSIPROP_ATTRIBTYPES_ONLY	= 0x4
ADSIPROP_SEARCH_SCOPE	= 0x5
ADSIPROP_TIMEOUT	= 0x6
ADSIPROP_PAGESIZE	= 0x7
ADSIPROP_PAGED_TIME_LIMIT	= 0x8
ADSIPROP_CHASE_REFERRALS	= 0x9
ADSIPROP_SORT_ON	= 0xa
ADSIPROP_CACHE_RESULTS	= 0xb
ADSIPROP_ADSIFLAG	= 0xc

# ADSI_DIALECT_ENUM
ADSI_DIALECT_LDAP	= 0
ADSI_DIALECT_SQL	= 0x1

# ADS_CHASE_REFERRALS_ENUM
ADS_CHASE_REFERRALS_NEVER	= 0
ADS_CHASE_REFERRALS_SUBORDINATE	= 0x20
ADS_CHASE_REFERRALS_EXTERNAL	= 0x40
ADS_CHASE_REFERRALS_ALWAYS	= ADS_CHASE_REFERRALS_SUBORDINATE | ADS_CHASE_REFERRALS_EXTERNAL

# Generated by h2py from ObjSel.h
DSOP_SCOPE_TYPE_TARGET_COMPUTER = 0x00000001
DSOP_SCOPE_TYPE_UPLEVEL_JOINED_DOMAIN = 0x00000002
DSOP_SCOPE_TYPE_DOWNLEVEL_JOINED_DOMAIN = 0x00000004
DSOP_SCOPE_TYPE_ENTERPRISE_DOMAIN = 0x00000008
DSOP_SCOPE_TYPE_GLOBAL_CATALOG = 0x00000010
DSOP_SCOPE_TYPE_EXTERNAL_UPLEVEL_DOMAIN = 0x00000020
DSOP_SCOPE_TYPE_EXTERNAL_DOWNLEVEL_DOMAIN = 0x00000040
DSOP_SCOPE_TYPE_WORKGROUP = 0x00000080
DSOP_SCOPE_TYPE_USER_ENTERED_UPLEVEL_SCOPE = 0x00000100
DSOP_SCOPE_TYPE_USER_ENTERED_DOWNLEVEL_SCOPE = 0x00000200
DSOP_SCOPE_FLAG_STARTING_SCOPE = 0x00000001
DSOP_SCOPE_FLAG_WANT_PROVIDER_WINNT = 0x00000002
DSOP_SCOPE_FLAG_WANT_PROVIDER_LDAP = 0x00000004
DSOP_SCOPE_FLAG_WANT_PROVIDER_GC = 0x00000008
DSOP_SCOPE_FLAG_WANT_SID_PATH = 0x00000010
DSOP_SCOPE_FLAG_WANT_DOWNLEVEL_BUILTIN_PATH = 0x00000020
DSOP_SCOPE_FLAG_DEFAULT_FILTER_USERS = 0x00000040
DSOP_SCOPE_FLAG_DEFAULT_FILTER_GROUPS = 0x00000080
DSOP_SCOPE_FLAG_DEFAULT_FILTER_COMPUTERS = 0x00000100
DSOP_SCOPE_FLAG_DEFAULT_FILTER_CONTACTS = 0x00000200
DSOP_FILTER_INCLUDE_ADVANCED_VIEW = 0x00000001
DSOP_FILTER_USERS = 0x00000002
DSOP_FILTER_BUILTIN_GROUPS = 0x00000004
DSOP_FILTER_WELL_KNOWN_PRINCIPALS = 0x00000008
DSOP_FILTER_UNIVERSAL_GROUPS_DL = 0x00000010
DSOP_FILTER_UNIVERSAL_GROUPS_SE = 0x00000020
DSOP_FILTER_GLOBAL_GROUPS_DL = 0x00000040
DSOP_FILTER_GLOBAL_GROUPS_SE = 0x00000080
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_DL = 0x00000100
DSOP_FILTER_DOMAIN_LOCAL_GROUPS_SE = 0x00000200
DSOP_FILTER_CONTACTS = 0x00000400
DSOP_FILTER_COMPUTERS = 0x00000800
DSOP_DOWNLEVEL_FILTER_USERS = (-2147483647)
DSOP_DOWNLEVEL_FILTER_LOCAL_GROUPS = (-2147483646)
DSOP_DOWNLEVEL_FILTER_GLOBAL_GROUPS = (-2147483644)
DSOP_DOWNLEVEL_FILTER_COMPUTERS = (-2147483640)
DSOP_DOWNLEVEL_FILTER_WORLD = (-2147483632)
DSOP_DOWNLEVEL_FILTER_AUTHENTICATED_USER = (-2147483616)
DSOP_DOWNLEVEL_FILTER_ANONYMOUS = (-2147483584)
DSOP_DOWNLEVEL_FILTER_BATCH = (-2147483520)
DSOP_DOWNLEVEL_FILTER_CREATOR_OWNER = (-2147483392)
DSOP_DOWNLEVEL_FILTER_CREATOR_GROUP = (-2147483136)
DSOP_DOWNLEVEL_FILTER_DIALUP = (-2147482624)
DSOP_DOWNLEVEL_FILTER_INTERACTIVE = (-2147481600)
DSOP_DOWNLEVEL_FILTER_NETWORK = (-2147479552)
DSOP_DOWNLEVEL_FILTER_SERVICE = (-2147475456)
DSOP_DOWNLEVEL_FILTER_SYSTEM = (-2147467264)
DSOP_DOWNLEVEL_FILTER_EXCLUDE_BUILTIN_GROUPS = (-2147450880)
DSOP_DOWNLEVEL_FILTER_TERMINAL_SERVER = (-2147418112)
DSOP_DOWNLEVEL_FILTER_ALL_WELLKNOWN_SIDS = (-2147352576)
DSOP_DOWNLEVEL_FILTER_LOCAL_SERVICE = (-2147221504)
DSOP_DOWNLEVEL_FILTER_NETWORK_SERVICE = (-2146959360)
DSOP_DOWNLEVEL_FILTER_REMOTE_LOGON = (-2146435072)
DSOP_FLAG_MULTISELECT = 0x00000001
DSOP_FLAG_SKIP_TARGET_COMPUTER_DC_CHECK = 0x00000002
CFSTR_DSOP_DS_SELECTION_LIST = "CFSTR_DSOP_DS_SELECTION_LIST"
