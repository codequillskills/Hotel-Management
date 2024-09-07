# URL
- API: /api/
- ADMIN: /admin/
- Filter: /api/filter/
- Reports: /reports/

# Notes
1. Hotel Table and Category Table is for **get** request only.
1. Guest Table and Booking Table is for **post** request only.
1. Admin Can Download **Reports** at any time.
1. In case of any updation of dates requested by the user admin can use **Filter** url (specified above) to check the number of rooms available during that period for the specific category with other filters also such as isConfirmed, isPaid, isCancelled, isRefund to avoid rejection if not available.
1. User can book room only if there is no overlapping in the dates for the particular category accoding to number of rooms available.
1. Particular mail will be send after value change for isConfirmed (for both true and false), isPaid, isCancelled, isRejected for the first time only.
1. If admin is changing the dates or any data from the booking, **no mail will be send again** after the updation.