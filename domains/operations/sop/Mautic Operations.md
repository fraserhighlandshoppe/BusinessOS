# SOP: Mautic Marketing Automation Operations

## Purpose

Standard operating procedure for managing Mautic marketing automation integrated with FrontAccounting and WooCommerce.

## Who

Marketing Operations agent, reviewed monthly by owner.

## When

- Daily: System health checks
- Weekly: Campaign performance review
- Monthly: Integration audit, feature updates

## Setup Checklist

### Initial Setup
- [ ] Mautic installed on hosting (shared or VPS)
- [ ] SSL certificate configured
- [ ] Database connection verified
- [ ] Cron jobs configured for cron.php and mailbox.php
- [ ] Webhook URLs generated in Mautic

### WooCommerce Integration
- [ ] WooCommerce webhook endpoint created
- [ ] Secret key configured
- [ ] Test order placed to verify sync
- [ ] Customer fields mapped in Mautic

### FA Integration
- [ ] API credentials configured
- [ ] Unsubscribe endpoint tested
- [ ] Purchase history import script scheduled
- [ ] Lead scoring rules validated

## Daily Operations

### 1. System Health Check
1. Log into Mautic
2. Check Dashboard for errors
3. Verify cron jobs ran successfully
4. Check webhook delivery logs
5. Review recent contact imports

### 2. Email Queue Monitoring
1. Check email queue status
2. Identify any stuck campaigns
3. Clear any failed deliveries
4. Review bounce rates

### 3. Unsubscribe Processing
1. Check Mautic → FA sync log
2. Verify opt-out records updated in FA
3. Flag any sync failures for investigation

## Weekly Operations

### 1. Campaign Performance Review
1. Run Email Performance report
2. Check open rates (target: >25%)
3. Check click rates (target: >3%)
4. Identify underperforming content
5. Adjust subject lines or content as needed

### 2. Lead Scoring Review
1. Check top-scoring contacts
2. Verify scoring accuracy
3. Adjust rules if needed
4. Update segments based on scores

### 3. Journey Builder Audit
1. Review active journeys
2. Check trigger conditions
3. Verify email content is current
4. Update seasonal content

## Monthly Operations

### 1. Integration Audit
1. Full sync test between all systems
2. Verify data accuracy across platforms
3. Check for duplicate contacts
4. Clean up old/inactive contacts

### 2. Feature Enhancement
1. Review new Mautic features
2. Plan implementation for next month
3. Update documentation
4. Train team on new features

### 3. Compliance Review
1. Verify unsubscribe processing
2. Check CASL/GDPR compliance
3. Review privacy policy alignment
4. Update consent records

## Troubleshooting

### Common Issues

#### Webhooks Not Working
1. Check WooCommerce webhook status
2. Verify Mautic endpoint is accessible
3. Check firewall/security settings
4. Test with manual API call

#### Contacts Not Syncing
1. Check for duplicate email addresses
2. Verify field mapping
3. Check API rate limits
4. Review error logs

#### Emails Not Sending
1. Check SMTP configuration
2. Review sender reputation
3. Check for spam filter blocks
4. Verify recipient list is valid

### Error Response Procedures

| Error | Immediate Action | Follow-up |
|---|---|---|
| Webhook failure | Check endpoint, retry | Document pattern |
| Sync timeout | Retry, check server load | Optimize queries |
| Duplicate contacts | Merge manually | Update dedupe rules |
| Email bounce | Suppress recipient | Review content |

## Data Management

### Contact Cleanup
- Remove contacts with no activity 12+ months
- Merge duplicates based on email
- Archive old segments
- Export backups monthly

### Backup Schedule
- Daily: Contact database
- Weekly: Campaign configurations
- Monthly: Full system backup

## Performance Metrics

### Email Metrics
| Metric | Target | Alert Threshold |
|---|---|---|
| Open Rate | >25% | <15% |
| Click Rate | >3% | <1% |
| Unsubscribe Rate | <0.5% | >1% |
| Bounce Rate | <2% | >5% |

### Integration Metrics
| Metric | Target | Alert Threshold |
|---|---|---|
| Sync Success Rate | >99% | <95% |
| Webhook Delivery | >99% | <95% |
| Contact Creation Time | <5 min | >30 min |

## Quality Checklist

- [ ] All webhooks delivering successfully
- [ ] No sync errors in past 24 hours
- [ ] Email deliverability within targets
- [ ] Lead scores accurate
- [ ] Segments properly populated
- [ ] Compliance requirements met
- [ ] Backups completed

## Related Documents

- `BR014 Mautic Marketing Automation` — Business requirements
- `Mautic Integration Strategy` — Full implementation guide
- `content/Channels/Email/Welcome Series.md` — Email content
- `DATA_CONTRACTS.md` — Data schemas