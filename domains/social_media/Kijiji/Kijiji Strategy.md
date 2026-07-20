# Kijiji Strategy

For dead stock liquidation and excess inventory.

## Objectives

- Convert idle inventory to cash flow
- Reach local buyers efficiently  
- Reduce warehouse holding costs
- Clear seasonal/clearance items
- Generate leads for future sales

## Target Products

| Category | Markup Strategy | Notes |
|---|---|---|
| Practice equipment | Cost × 1.5-1.75 | High turnover |
| Reeds/accessories | Cost × 1.75 | Competitive category |
| Giftware | Cost × 1.5 | Seasonal items |
| Highland dress basics | Cost × 1.5-2.0 | Kilts, sporrans, jewelry |
| Books/CDs | Cost × 1.5 | Educational products |
| Competition gear | Cost × 1.5 | Used but well-maintained |

## Out of Scope

- High-end bagpipes/drums (handle via direct sales)
- Custom orders
- Items requiring repair
- International shipping (local pickup only)
- Items over $500 (marketplace preferred)

## Listing Requirements

### Title Format
`[Category] - [Brand] - [Model] - [Condition]`
Example: `Practice Chanter - Sirocco - Kintail - Like New`

### Description Template
```
Excellent condition [item description]. 

Originally purchased for [reason]. 
Never used / lightly used / stored in smoke-free environment.

Local pickup only from Calgary/Airdrie. 
Phone: [store phone] 
Serious inquiries welcome!

#HighlandDance #Bagpipes #Calgary #Kijiji
```

### Photo Requirements
- Minimum 5 photos (Kijiji requires more than Facebook)
- White background for main shot
- Include scale reference
- Show any wear or defects
- Use consistent lighting
- Include close-ups of key features

## Pricing Strategy

| Condition | Multiplier |
|---|---|
| New, unopened | Cost × 2.0 |
| Like new | Cost × 1.75 |
| Very good | Cost × 1.5 |
| Good | Cost × 1.25 |
| Fair | Cost × 1.0 |

**Minimum floor**: Cost × 1.0 for all items (Kijiji has lower price tolerance)

## Kijiji-Specific Considerations

### Fees
- Featured ads: $5-20 CAD (optional)
- Bold titles: $2-5 CAD
- Highlight: $2-3 CAD
- **Plan to spend ~$10-15 per listing for visibility**

### Categories
- **Music Instruments** > Musical Instruments > Winds, Brass & Percussion
- **Collectibles** > Music Memorabilia
- **Books** > Educational & Professional
- **Clothing** > Costumes & Accessories

### Search Optimization
- Use keywords: "bagpipes," "piping," "highland dance," "scottish"
- Include location in title: "Calgary" or "Airdrie"
- Use popular search terms from Kijiji search autocomplete

## Automation Workflow

1. **Daily**: Query FA for items with `stock > 0` AND `last_sold_date < 180 days`
2. **Filter**: Exclude high-value items, reserved stock
3. **Generate**: CSV with product data + calculated prices
4. **Create Listings**: Use Kijiji bulk upload or API
5. **Monitor**: Check daily for inquiries, update status
6. **Sync**: Nightly check for sold status, update FA inventory

## Performance Tracking

- Conversion rate (inquiries to sales)
- Average days to sell
- Profit margin after Kijiji fees
- Customer feedback/repeat buyers
- Cost per acquisition

## Compliance

- CASL compliance in descriptions
- Accurate product condition
- No prohibited items (per Kijiji policy)
- Clear pickup terms
- Include GST/HST in pricing where applicable

## Comparison: Facebook Marketplace vs Kijiji

| Aspect | Facebook Marketplace | Kijiji |
|---|---|---|
| Audience | Facebook users, wider reach | Kijiji users, more purchase intent |
| Fees | Free | $5-20 per featured ad |
| Photos | 1-10 | 5-25 |
| Categories | Broad | More specific |
| Search | Social graph | Location-based |
| Best For | Community trust, impulse buys | Serious buyers, local |

## Integration with Facebook Marketplace

- List on both platforms for maximum reach
- Use same photos and descriptions
- Track performance separately
- Cross-promote items between platforms