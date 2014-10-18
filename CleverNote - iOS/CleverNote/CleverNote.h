//
//  CleverNote.h
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import <Foundation/Foundation.h>

@class CleverNote;

@protocol CleverNoteDelegate <NSObject>

@optional

-(void) cleverNote:(CleverNote *)chat didLoadNotes:(NSArray *) notes;

@end

@interface CleverNote : NSObject

@property (strong, nonatomic) id<CleverNoteDelegate> delegate;
@property (strong, nonatomic) NSString *accessToken;

@property (strong, nonatomic) NSURLComponents *urlBuilder;

-(void) loadNotes;

@end
