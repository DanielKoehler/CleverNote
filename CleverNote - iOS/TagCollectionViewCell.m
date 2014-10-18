//
//  TagCollectionViewCell.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "TagCollectionViewCell.h"

@implementation TagCollectionViewCell

- (id)initWithFrame:(CGRect)frame reuseIdentifier:(NSString *)reuseIdentifier {
    
    self = [super initWithFrame:frame];
    
    return self;
    
}

-(void) setTitle:(NSString *)title {
    
    [self setBackgroundColor:[UIColor colorWithRed:52.0f/255 green:152.0f/255 blue:219.0f/255 alpha:1.0f]];
    self.tagLabel.text = title;
    self.tagLabel.textColor = [UIColor whiteColor];
    self.layer.cornerRadius = 15.0;
    self.layer.masksToBounds = YES;
    
    
}

@end
