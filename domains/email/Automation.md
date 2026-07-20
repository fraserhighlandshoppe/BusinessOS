# Email Automation

MailPoet automation workflows.

## Setup Checklist

- [ ] Create/list segments (daily, weekly, monthly).
- [ ] Build signup forms (site + social + Games booth).
- [ ] Configure CAN-SPAM / CASL compliance (unsubscribe, sender identity).
- [ ] Import/seed subscriber list from FrontAccounting customers.
- [ ] Build the 3-email welcome sequence.
- [ ] Add referral-coupon block to every template.
- [ ] Monitor reputation/SPAM scores (authentication, clean list).

## Segments

See `Segments.md` for definitions and FA import query.

## Welcome Series

See `Welcome Series.md` for content and timing.

## Automation Triggers

| Trigger | Action | Delay |
|---|---|---|
| New subscriber | Send welcome email 1 | Immediately |
| New subscriber | Send welcome email 2 | 1 day |
| New subscriber | Send welcome email 3 | 3 days |
| No engagement after 30 days | Add to re-engagement segment | 30 days |
| Birthday | Send birthday offer | Date field |

## Referral Program

- Every newsletter includes referral coupon code
- Track referrals via unique codes
- Quarterly top referrers featured in newsletter
- Annual referral contest with prizes

## A/B Testing

- Subject lines: Test 2 variants, send to 10% each
- Send times: Test 9am vs 2pm vs 6pm
- CTAs: Test "Shop Now" vs "View Collection"
- Content length: Test short vs long format

## Metrics to Track

- Open rate (target: >25%)
- Click-through rate (target: >3%)
- Conversion rate (target: >1%)
- Unsubscribe rate (target: <0.5%)
- List growth rate (target: >5%/month)