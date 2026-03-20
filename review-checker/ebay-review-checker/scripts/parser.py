#!/usr/bin/env python3
"""
Review Parser - Multi-format Input Parser
ReviewParse -  many FormatInputParse

SupportFormat:
- pureText (Paragraph separator)
- JSON
- CSV
- TSV
- Markdown Table

Version: 1.0.0
"""

import json
import csv
import re
from typing import List, Optional
from dataclasses import dataclass
from io import StringIO


@dataclass
class Review:
    """Single itemReview"""
    content: str
    rating: Optional[int] = None
    date: Optional[str] = None
    reviewer_name: Optional[str] = None
    verified_purchase: Optional[bool] = None
    helpful_votes: Optional[int] = None
    reviewer_reviews_count: Optional[int] = None


class ReviewParser:
    """ many FormatReviewParse"""
    
    @staticmethod
    def detect_format(text: str) -> str:
        """DetectionInputFormat"""
        text = text.strip()
        
        # JSON group
        if text.startswith('[') and text.endswith(']'):
            try:
                json.loads(text)
                return 'json'
            except:
                pass
        
        # JSON Object
        if text.startswith('{'):
            try:
                json.loads(text)
                return 'json_single'
            except:
                pass
        
        # CSV (CheckComma separated with header)
        lines = text.split('\n')
        if len(lines) > 1:
            first_line = lines[0].lower()
            if ',' in first_line and any(h in first_line for h in ['content', 'review', 'rating', 'date', 'text']):
                return 'csv'
        
        # TSV
        if len(lines) > 1 and '\t' in lines[0]:
            return 'tsv'
        
        # Markdown Table
        if '|' in text and '---' in text:
            return 'markdown'
        
        # DefaultpureText
        return 'text'
    
    @staticmethod
    def parse(text: str) -> List[Review]:
        """ParseReview"""
        format_type = ReviewParser.detect_format(text)
        
        parsers = {
            'json': ReviewParser.parse_json,
            'json_single': ReviewParser.parse_json_single,
            'csv': ReviewParser.parse_csv,
            'tsv': ReviewParser.parse_tsv,
            'markdown': ReviewParser.parse_markdown,
            'text': ReviewParser.parse_text,
        }
        
        parser = parsers.get(format_type, ReviewParser.parse_text)
        return parser(text)
    
    @staticmethod
    def parse_json(text: str) -> List[Review]:
        """Parse JSON group"""
        try:
            data = json.loads(text)
            reviews = []
            for item in data:
                review = Review(
                    content=item.get('content', item.get('text', item.get('review', ''))),
                    rating=item.get('rating', item.get('stars', item.get('star'))),
                    date=item.get('date', item.get('review_date')),
                    reviewer_name=item.get('reviewer_name', item.get('author', item.get('name'))),
                    verified_purchase=item.get('verified_purchase', item.get('vp', item.get('verified'))),
                    helpful_votes=item.get('helpful_votes', item.get('helpful')),
                )
                if review.content:
                    reviews.append(review)
            return reviews
        except:
            return []
    
    @staticmethod
    def parse_json_single(text: str) -> List[Review]:
        """ParseSingle JSON Object"""
        try:
            item = json.loads(text)
            review = Review(
                content=item.get('content', item.get('text', item.get('review', ''))),
                rating=item.get('rating', item.get('stars')),
                date=item.get('date'),
                reviewer_name=item.get('reviewer_name', item.get('author')),
                verified_purchase=item.get('verified_purchase', item.get('vp')),
            )
            return [review] if review.content else []
        except:
            return []
    
    @staticmethod
    def parse_csv(text: str) -> List[Review]:
        """Parse CSV"""
        reviews = []
        try:
            reader = csv.DictReader(StringIO(text))
            for row in reader:
                # TryMultipleField name
                content = (
                    row.get('content') or row.get('Content') or
                    row.get('review') or row.get('Review') or
                    row.get('text') or row.get('Text') or
                    row.get('review_text') or row.get('body') or ''
                )
                
                rating_str = (
                    row.get('rating') or row.get('Rating') or
                    row.get('stars') or row.get('Stars') or
                    row.get('star') or ''
                )
                rating = None
                if rating_str:
                    try:
                        rating = int(float(rating_str))
                    except:
                        pass
                
                date = (
                    row.get('date') or row.get('Date') or
                    row.get('review_date') or row.get('created_at') or None
                )
                
                vp_str = (
                    row.get('verified_purchase') or row.get('vp') or
                    row.get('verified') or row.get('VP') or ''
                )
                vp = None
                if vp_str:
                    vp = vp_str.lower() in ['true', 'yes', '1', 'y', 'verified']
                
                reviewer = (
                    row.get('reviewer_name') or row.get('author') or
                    row.get('name') or row.get('reviewer') or None
                )
                
                if content:
                    reviews.append(Review(
                        content=content,
                        rating=rating,
                        date=date,
                        reviewer_name=reviewer,
                        verified_purchase=vp,
                    ))
        except Exception as e:
            print(f"CSV parse error: {e}")
        
        return reviews
    
    @staticmethod
    def parse_tsv(text: str) -> List[Review]:
        """Parse TSV"""
        # Convert to CSV FormatProcess
        csv_text = text.replace('\t', ',')
        return ReviewParser.parse_csv(csv_text)
    
    @staticmethod
    def parse_markdown(text: str) -> List[Review]:
        """Parse Markdown Table"""
        reviews = []
        lines = text.strip().split('\n')
        
        # find to Tablehead
        header_line = None
        data_start = 0
        for i, line in enumerate(lines):
            if '|' in line and '---' not in line:
                header_line = line
                data_start = i + 2  # Skip separator lines
                break
        
        if not header_line:
            return []
        
        # ParseTablehead
        headers = [h.strip().lower() for h in header_line.split('|') if h.strip()]
        
        # ParseDatarow
        for line in lines[data_start:]:
            if '|' not in line:
                continue
            
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) < len(headers):
                continue
            
            row = dict(zip(headers, cells))
            
            content = row.get('content', row.get('review', row.get('text', '')))
            rating = None
            rating_str = row.get('rating', row.get('stars', ''))
            if rating_str:
                try:
                    rating = int(float(rating_str.replace('★', '').strip()))
                except:
                    pass
            
            if content:
                reviews.append(Review(
                    content=content,
                    rating=rating,
                    date=row.get('date'),
                    reviewer_name=row.get('author', row.get('reviewer')),
                ))
        
        return reviews
    
    @staticmethod
    def parse_text(text: str) -> List[Review]:
        """ParsepureText"""
        reviews = []
        
        # TrySplit by paragraph
        paragraphs = re.split(r'\n\n+', text.strip())
        
        for para in paragraphs:
            para = para.strip()
            if len(para) < 10:
                continue
            
            review = Review(content=para)
            
            # TryExtract starLevel
            star_patterns = [
                r'(\d)\s*(?:star|stars|★|⭐)',
                r'(?:star|stars|rating)[:\s]*(\d)',
                r'^(\d)★',
                r'^(\d)\s*star',
            ]
            for pattern in star_patterns:
                match = re.search(pattern, para, re.I)
                if match:
                    review.rating = int(match.group(1))
                    break
            
            # TryExtractDayPeriod
            date_patterns = [
                r'(\d{4}-\d{2}-\d{2})',
                r'(\w+\s+\d{1,2},?\s+\d{4})',
                r'(\d{1,2}/\d{1,2}/\d{4})',
            ]
            for pattern in date_patterns:
                match = re.search(pattern, para)
                if match:
                    review.date = match.group(1)
                    break
            
            # TryExtract VP Status
            if re.search(r'verified\s*purchase', para, re.I):
                review.verified_purchase = True
            elif re.search(r'not\s*verified', para, re.I):
                review.verified_purchase = False
            
            reviews.append(review)
        
        return reviews


def parse_reviews(text: str) -> List[Review]:
    """ConvenientFunction"""
    return ReviewParser.parse(text)


# CLI
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        # TestData
        text = """
content,rating,date,verified_purchase
"Great product!",5,2024-01-15,true
"Not good",2,2024-01-16,false
"Amazing!",5,2024-01-17,true
"""
    
    reviews = parse_reviews(text)
    print(f"Parsed {len(reviews)} reviews:")
    for r in reviews:
        print(f"  - {r.rating}★ | VP:{r.verified_purchase} | {r.content[:50]}...")
