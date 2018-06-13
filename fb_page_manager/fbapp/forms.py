from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

# not used
class SimpleForm(forms.Form):
    name = forms.CharField(label="Page Name", required=False)
    about = forms.CharField(label="About Page", required=False)
    bio = forms.CharField(label="Bio", required=False)
    website = forms.CharField(label="Website", required=False)
    phone = forms.CharField(label="Phone", required=False)
    whatsapp_number = forms.CharField(label="Whatsapp Number", required=False)
    general_info = forms.CharField(label="General Info", required=False)

    impressum = forms.CharField(label="Impressum", required=False)
    description = forms.CharField(label="Description", required=False)
    company_overview = forms.CharField(label="Company Overview", required=False)
    hello = forms.CharField(required=False)

    #category = forms.CharField(label="Page Category", required=False)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Field("hello", type="hidden", hidden=True)
    )


#################  FB API RESPONSE DETAILS BEWLOWWWWWWWWWWWWWWWWWWWWWWW

'''
fb page categories
ACTIVITY_GENERAL
COMMUNITY_ORGANIZATION
MEDIA
CONCERT_TOUR
PERSON
SUPER_BUSINESS
COMMERCIAL_BANK

impressum, whatsapp_number,phone
displayed_message_response_time,fan_count,link,overall_star_rating,rating_count,verification_status,is_published
fancount int
star_rating float
rating count float
is_published bool

{
                "description": "The emails listed in the About section of a Page",
                "type": "list<string>",
                "name": "emails"
            },
{
                "description": "Page estimated message response time displayed to user",
                "type": "string",
                "name": "displayed_message_response_time"
            },

{
                "description": "The number of users who like the Page. For Global Pages this is the count for all Pages across the brand",
                "type": "unsigned int32",
                "name": "fan_count"
            },
{
                "description": "General information provided by the Page",
                "type": "string",
                "name": "general_info"
            }
{
                "description": "has whatsapp number",
                "type": "bool",
                "name": "has_whatsapp_number"
            }
{
                "description": "Indicates a single range of opening hours for a day. Each day can have 2 different hours ranges. The keys in the map are in the form of `{day}_{number}_{status}`.  `{day}` should be the first 3 characters of the day of the week, `{number}` should be either 1 or 2 to allow for the two different hours ranges per day. `{status}` should be either `open` or `close` to delineate the start or end of a time range. An example would be `mon_1_open` with value `17:00` and `mon_1_close` with value `21:15` which would represent a single opening range of 5pm to 9:15pm on Mondays",
                "type": "map<string, string>",
                "name": "hours"
            }
{
                "description": "Legal information about the Page publishers",
                "type": "string",
                "name": "impressum"
            },
{
                "description": "Indicates whether this location is always open",
                "type": "bool",
                "name": "is_always_open"
            }
 {
                "description": "The Page's Facebook URL",
                "type": "string",
                "name": "link"
            },
{
                "description": "Overall page rating based on rating survey from users on a scale of 1-5. This value is normalized and is not guaranteed to be a strict average of user ratings.",
                "type": "float",
                "name": "overall_star_rating"
            },

 {
                "description": "Phone number provided by a Page",
                "type": "string",
                "name": "phone"
            },
{
                "description": "Number of ratings for the page (limited to ratings that are publicly accessible)",
                "type": "unsigned int32",
                "name": "rating_count"
            },
 {
                "description": "Showing whether this Page is verified and in what color e.g. blue verified, gray verified or not verified",
                "type": "string",
                "name": "verification_status"
            },
 {
                "description": "whatsapp number",
                "type": "string",
                "name": "whatsapp_number"
            },

{
                "description": "Indicates whether the Page is published and visible to non-admins",
                "type": "bool",
                "name": "is_published"
            },

'''