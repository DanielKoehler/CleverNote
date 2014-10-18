//
//  TagCollectionViewCell.h
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface TagCollectionViewCell : UICollectionViewCell

@property (nonatomic, strong) IBOutlet UILabel *tagLabel;

@property (nonatomic, strong) NSString *title;

@end
