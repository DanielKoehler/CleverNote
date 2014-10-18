//
//  NotesTableViewCell.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//


#import "NotesTableViewCell.h"

@implementation NotesTableViewCell

- (void) awakeFromNib {
    // Initialization code
    
    [super awakeFromNib];
    
    NSLog(@"Here");
    
    self.titleLabel.text  = self.note.title;
    self.excerpLabel.text = self.note.content;
    
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    [formatter setDateFormat:@"dd/mm/yyyy"];
    
//    [formatter setTimeZone:[NSTimeZone timeZoneWithName:@"gmt"]];
    
    NSString *stringFromDate = [formatter stringFromDate:self.note.updated];
    
    self.dateLabel.text = stringFromDate;
    
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
    
    
    
}

@end
