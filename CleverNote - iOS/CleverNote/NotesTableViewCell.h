//
//  NotesTableViewCell.h
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "Note.h"

@interface NotesTableViewCell : UITableViewCell

@property (strong, nonatomic) IBOutlet UILabel *titleLabel;

@property (strong, nonatomic) IBOutlet UILabel *excerpLabel;

@property (strong, nonatomic) IBOutlet UILabel *dateLabel;

@property (strong, nonatomic) IBOutlet UICollectionView *tagCollectionView;


@property (strong, nonatomic) Note *note;

@end
