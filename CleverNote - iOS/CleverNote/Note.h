//
//  Note.h
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Note : NSObject

@property (strong, nonatomic) NSString *guid;
@property (strong, nonatomic) NSString *title;	//string
@property (strong, nonatomic) NSString *content;	//string
@property (strong, nonatomic) NSString *contentHash;	//string
@property (nonatomic) NSInteger *contentLength;	//i32

@property (strong, nonatomic) NSDate *created;	//Timestamp
@property (strong, nonatomic) NSDate *updated ;	//Timestamp
@property (strong, nonatomic) NSDate *deleted;	//Timestamp
@property (nonatomic) BOOL active;	//bool
@property (nonatomic) NSInteger *updateSequenceNum;	//i32
@property (strong, nonatomic) NSString *notebookGuid;	//string
@property (strong, nonatomic) NSArray *tagGuids;	//list<Guid>
@property (strong, nonatomic) NSArray *resources;	//list<Resource>
//@property (strong, nonatomic) attributes	NoteAttributes
@property (strong, nonatomic) NSArray *tagNames;
@property (strong, nonatomic) NSArray *tags;

-(id) initWithJSONEncodedRepresentation:(NSDictionary *) json;

-(id) testNote;

@end
