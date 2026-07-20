# Email Segments

Customer segmentation strategy for targeted messaging.

## Segment Definitions

### Daily Piping Enthusiasts
- **Criteria**: Open rates > 50% on piping content, frequent website visitors
- **Size**: ~15% of list
- **Content**: Daily piping tips, new bagpipe arrivals, school updates
- **Frequency**: Daily digest email

### Weekly Drummers
- **Criteria**: Purchased drumming equipment, engages with drum content
- **Size**: ~20% of list
- **Content**: Weekly drum practice tips, new sticks/heads, gig announcements
- **Frequency**: Weekly summary

### Monthly Dance Community
- **Criteria**: Purchased dance items, follows dance social accounts
- **Size**: ~10% of list
- **Content**: Monthly dance outfit inspiration, shoe care, competition dates
- **Frequency**: Monthly roundup

### Occasional Gift Buyers
- **Criteria**: Seasonal purchases, low email engagement
- **Size**: ~30% of list
- **Content**: Holiday gift guides, clearance items, gift certificates
- **Frequency**: Bi-weekly

### Studio/Educator Network
- **Criteria**: Business email domains, bulk orders, contact form submissions
- **Size**: ~10% of list
- **Content**: Bulk order discounts, equipment for classes, teacher resources
- **Frequency**: Weekly

### Inactive Subscribers
- **Criteria**: No opens in 60 days, no purchases in 90 days
- **Size**: ~15% of list
- **Content**: Re-engagement campaign, special offers
- **Frequency**: Monthly

## Segment Migration Rules

- Customers who purchase in a segment's category move to that segment
- Engagement level determines frequency
- Purchases in multiple categories: assign to primary interest

## Import from FA

```sql
SELECT 
    email,
    first_name,
    last_name,
    CASE 
        WHEN order_category = 'piping' THEN 'daily_piping'
        WHEN order_category = 'drumming' THEN 'weekly_drumming'
        WHEN order_category = 'dance' THEN 'monthly_dance'
        ELSE 'occasional_gift'
    END as segment
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date > DATE_SUB(NOW(), INTERVAL 1 YEAR)
```